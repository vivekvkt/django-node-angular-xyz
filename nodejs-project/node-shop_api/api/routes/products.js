const express = require('express')

const route = express.Router();
const mongoose = require('mongoose')
const multer = require('multer');

const checkAuth = require('../middleware/check-auth')

const storage = multer.diskStorage({
    destination:function(req,file,cb){
        cb(null, './uploads/');
    },
    filename:function(req,file,cb){
        cb(null,new Date().toISOString()+ file.originalname);
    }
});

const fileFilter = (req,file,cb)=>{
    // reject file
    if(file.mimetype ==='image/jpeg' || file.mimetype==='image/png'){
        cb(null,true);
    }
    else{
        cb(null,false);
    } 
};


const upload = multer({
    storage:storage,
    limits:{
    fileSize:1024 *1024 *5
},
fileFilter:fileFilter
});

const Product  = require('../models/product');

route.get('/',(req,res,next)=>{
        Product.find()
        .select('name price _id productImage')
        .exec()
        .then(data=>{
            const response = {
                count : data.length,
                products:data.map(res=>{
                    return {
                        name:res.name,
                        price:res.price,
                        productImage:res.productImage,
                        _id:res._id,
                        request :{
                            type:'GET',
                            url:'http://localhost:3000/products/' +res._id
                        }
                    }
                })
            };
            res.status(200).json({
                data:response
            });
        })
        .catch(error=>{
            res.status(500).json({
                error:error
            })
        })
       
});

route.get('/:productId',(req,res,next)=>{
    const id = req.params.productId
    Product.findById(id)
    .select('name price _id productImage')
    .exec()
    .then(doc =>{
        if(doc){
        res.status(200).json({
         product:doc,
         request:{
             type:'GET',
             descriptions:"Get all product",
             url:'http://localhost:3000/products'
         }
        });
        }
        else{
            res.status(404).json({message:"provided id is not found"}); 
        }
    })
    .catch(err=>{
        console.log(err)
        res.status(500).json({error:err});
    })
});

route.post('/', checkAuth,upload.single('productImage'),(req,res,next)=>{
    console.log(req.file)
    const product = new Product({
        _id:mongoose.Types.ObjectId(),
        name :req.body.name,
        price:req.body.price,
        productImage:req.file.path
    });
    product.save()
    .then(result =>{
        console.log(result);
        res.status(201).json({
            message:'Object has been created successfully',
            createdProduct:{
                name:result.name,
                price:result.price,
                _id:result._id,
                request:{
                    type:'GET',
                    url:'http://localhost:3000/products/' +result._id
                }
            }
        })

    })
    .catch(err=>{
        console.log(err)
        res.status(500).json({
            error:err
        });
        
    });   
})


route.put('/:productId',(req,res,next)=>{
    const id = req.params.productId
    Product.findByIdAndUpdate(id)
    .exec()
    .then(data=>{
        res.status(200).json({
            data:data
        });
    })
    .catch(error=>{
        res.status(500).json({
            error:err
        });
    }) ;
});


route.patch('/:productId',checkAuth,(req,res,next)=>{
    const id = req.params.productId
    const updateOps = {};
    for (const ops  of req.body){
        updateOps[ops.propName] = ops.value;
    }
    Product.update(
        {_id:id},{$set:updateOps})
        .exec()
        .then(result=>{
            console.log(result)
            res.status(200).json(result)
        })
        .catch(err=>{
            console.log(err)
            res.status(500).json({
                error:err
            })
        })   
});

route.delete('/:productId',checkAuth,(req,res,next)=>{
    const id = req.params.productId;
    Product.deleteOne({_id:id})
    .exec()
    .then(res=>{
        res.status(200).json({
            message:'Provided item id has been deleted',
            request:{
                type:'POST',
                url:'http://localhost:3000/products',
                body:{name:'String',price:'Number'}
            }

        });
    })
    .catch(err=>{
        res.status(500).json({
            errr:err
        });
    }); 
});


module.exports = route