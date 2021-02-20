const express = require('express')
const mongoose = require('mongoose')
const router =  express.Router();

const Product = require('../models/product')

//handlin incoming get request product api

router.get('/',(req,res,next)=>{
    Product.find().sort( { _id: -1 } )
    .exec()
    .then(docs=>{
        if (docs){
            res.status(200).json({"docs":docs})
        }
        else{
            res.status(404).json({
                message:'No data found'
            })
        }
        
    })
    .catch(error=>{
        res.status(500).json({error:error})
    })

})


router.get('/:productId',(req,res,next)=>{
    const id = req.params.productId
    Product.findById(id)
    .exec()
    .then(doc=>{
        console.log(doc)
        if (doc){
            res.status(200).json(doc); 
        }
        else {
            res.status(404).json({
                message:"no valid data found.please provide valid ID"
            })
        }
         
    })
    .catch(error=>{
        console.log(error)
        res.status(500).json({error:error})
    })


})



router.post('/',(req,res,next)=>{
    const product = new Product({
        _id: new mongoose.Types.ObjectId(),
        name:req.body.name,
        price:req.body.price
    });
    product.save().then(result=>{
        console.log(result);
        res.status(201).json({
            "result":result
        })
       
    }).catch(error=>{
        console.log(error)
        res.status(500).json({error:error})
    });
   
    
})


router.put('/:productId',(req,res,next)=>{
    productId = req.params.productId

    if (productId=='update'){
        res.status(200).json({
            message:"Getting Product Id",
            id:productId
        })
    }
    else{
        res.status(200).json({
            message:"you nees to pass Id for update"
        })
    }

   
})

router.patch('/:productId',(req,res,next)=>{
    const id  = req.params.productId
    const updateOps = {}
    for (const ops of req.body){
        updateOps[ops.propName]=ops.value
    }

    Product.updateOne({_id:id}, {$set:updateOps})
    .exec() 
    .then(result=>{
        res.status(200).json({"message":"Updated","result":result})
    })
    .catch(error=>{
        res.status(500).json({error:error})
    })

   

   
})

router.delete('/:productId',(req,res,next)=>{
    const id  = req.params.productId
    Product.remove({_id:id})
    .exec()
    .then(result=>{
        res.status(200).json({
            "message":"data has been deleted.",
            "result":result
        })
    })
    .catch(error=>{
        res.status(500).json({error:error})
    })

})

module.exports = router;