const express = require('express');

const app = express();
const morgan = require('morgan')

const bodyParser = require('body-parser')

const mongoose = require('mongoose')
const productRouter = require('./api/routes/products');
const orderRouter = require('./api/routes/orders');
const UserRoutes = require('./api/routes/user');

const url = 'mongodb://127.0.0.1:27017/myshop_api'

//'mongodb://127.0.0.1:27017'
mongoose.connect(url,{
    useMongoClient:true
});
const db = mongoose.connection
db.once('open', _ => {
  console.log('Database connected:', url)
})

db.on('error', err => {
  console.error('connection error:', err)
})

mongoose.Promise = global.Promise;
app.use(morgan('dev'));
app.use('/uploads',express.static('uploads'));
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

app.use((req,res,next)=>{
    res.header('Acsess-Control-Allow-Origin','*');
    res.header('Access-Control-Allow-Headers',
    "Origin, X-Requested-With, Content-Type, Accept, Authorization"
    );
    if (req.method==='OPTIONS'){
        res.header('Access-Control-Allow-MethodS','PUT,POST,PATCH,DELETE GET');
        return res.status(200).json({})
    }
    next();
});

app.use('/products',productRouter);
app.use('/orders',orderRouter);
app.use('/user',UserRoutes);


app.use((req,res,next)=>{
  const error = Error('Not Found')
  error.status = 404;
  next(error)
});

app.use((error,req,res,next)=>{
    res.status(error.status || 500);
    res.json({
        error :{
            message:error.message
        }
    })
})

module.exports = app;