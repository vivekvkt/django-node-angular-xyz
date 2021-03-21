const express =  require('express')
const app =  express();
const morgan = require('morgan')
const mongoose = require('mongoose')
const MongoClient = require("mongodb");
const bodyParser =  require('body-parser')

const productsRoutes = require('./api/routes/products')
const orderRoutes = require('./api/routes/orders')

// database configurations
const url = 'mongodb://127.0.0.1:27017/myshop_api'

//'mongodb://127.0.0.1:27017'
mongoose.connect(url,{
    useNewUrlParser:true
});
const db = mongoose.connection
db.once('open', _ => {
  console.log('Database connected:', url)
})

db.on('error', err => {
  console.error('connection error:', err)
})

mongoose.Promise = global.Promise;



app.use(morgan('dev'))
app.use(bodyParser.urlencoded({extended:false}))
app.use(bodyParser.json());
app.use((req,res, next)=>{
    res.header('Access-Control-Allow-Origin','*')
    res.header("Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accepted,Authorization")

    if (req.method=='OPTIONS'){
        res.header('Access-Control-Allow-Methods','POST,GET,PUT,PATCH,DELETE')
        return res.status(200).json({

        })
    }
    next();
});

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