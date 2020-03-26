const express = require('express')

const route = express()
const mongoose = require('mongoose')

const Order = require('../models/order')
const Product = require('../models/product')
const checkAuth = require('../middleware/check-auth');

route.get('/',checkAuth,(req,res,next)=>{
  Order.find()
  .select('quantity product _id')
  .populate('product','name')
  .exec()
  .then(result=>{
      res.status(200).json({
          message:"get data successfully",
          count:result.length,
          order:result.map(res=>{
              return {
                  _id:res._id,
                  product:res.product,
                  quantity:res.quantity,
                  request:{
                    type:'GET',
                    url:'http://localhost:300/orders/' + res._id
                }
              }
          })
      });
  })
  .catch(error=>{
      res.status(500).json({
          error:error
      })
  })     
});



route.get('/:orderId',checkAuth,(req,res,next)=>{
    const orderId = req.params.orderId

    Order.findById(orderId)
    .populate('product')
    .exec()
    .then(order=>{
        if(!order){
            return res.status(404).json({message:"Requested Order not found"})
        }
        res.status(200).json({
            order:order,
            request:{
                type:'GET',
                description:"GET ALL DATA",
                url:'http:localhost:3000/orders'
            }
        });
    })
    .catch(err=>{
        res.status(500).json({
           error:err 
        })
    });
});

route.post('/',checkAuth,(req,res,next)=>{
    Product.findById(req.body.productId)
    .then(product=>{
        
        if(!product){
            console.log("hello")
           return res.status(404).json({message:"product not found"});
        }
        const order = new Order({
            _id:mongoose.Types.ObjectId(),
             quantity:req.body.quantity,
             product:req.body.productId
         });
        return  order.save()
         .then(result=>{
            res.status(201).json({
                message:'order successfully',
                order: {
                    _id:result._id,
                    product:result.product,
                    quantity:result.quantity
                },
                request :{
                    type:'GET',
                    url:'http://localhost:300/orders/' + result._id
                }
            });
         })
         .catch(err=>{
            res.status(500).json({err:err})
         });
        });
    });



route.put('/:orderId',checkAuth,(req,res,next)=>{

    res.status(200).json({
        message:'Handling Request PUT method'
    })
})


route.patch('/:orderId',checkAuth,(req,res,next)=>{

    res.status(200).json({
        message:'update order'
    })
})

route.delete('/:orderId',checkAuth,(req,res,next)=>{

    Order.remove({_id:req.params.orderId})
    .exec()
    .then(order=>{
        res.status(200).json({
            message:'Order has been deleted',
            orderId:req.params.orderId,
            request:{
                type:'POST',
                url:"http://localhost:3000/orders",
                body:{productId:"ID", quantity:"Number"}
            }
        })
    })
    .catch(err=>{
        res.status(500).json({
            error:err
        })
    })
})


module.exports = route