const express =  require('express')
const app =  express();
const morgan = require('morgan')

const productsRoutes = require('./api/routes/products')
const orderRoutes = require('./api/routes/orders')

app.use(morgan('dev'))

app.use('/products', productsRoutes);
app.use('/orders', orderRoutes);

// add middleware for handling error

app.use((req,res,next)=>{
    const error = new Error("Not Found")
    error.status=404;
    next(error)
})

app.use((error,req,res,next)=>{
   // handling any types of error 
   res.status( error.status || 500);
   res.json({
       error:{
           message:error.message
       }
   })

})



module.exports = app;