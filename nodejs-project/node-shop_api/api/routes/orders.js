const express = require('express')

const route = express()
const mongoose = require('mongoose')

// const Order = require('../models/order')

const Product = require('../models/product')
const checkAuth = require('../middleware/check-auth');

const OrdersControllers = require( '../controllers/orders');

const getOrderByIdControllers = require('../controllers/orders');

const createOrderControllers = require('../controllers/orders');

const deleterOrderControllers = require('../controllers/orders')





route.get('/', checkAuth,OrdersControllers.orders_getAll);

route.get('/:orderId',checkAuth,getOrderByIdControllers.getorderById);

route.post('/',checkAuth,createOrderControllers.create_order);

route.delete('/:orderId',checkAuth,deleterOrderControllers.delete_order)



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




module.exports = route