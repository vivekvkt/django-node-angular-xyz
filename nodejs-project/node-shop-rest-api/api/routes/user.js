const express = require('express')
const route = express.Router();
const mongoose = require('mongoose')
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const User = require('../models/users');

route.post('/signup',(req,res,next)=>{

 User.find({email:req.body.email})
 .exec()
 .then(user=>{
     if(user.length>=1){
         return res.status(409).json({
             message:"User email already exist"
         });
     }
     else{

        bcrypt.hash(req.body.password,10,(err,hash)=>{
            if(err){
                console.log(err)
                return res.status(500).json({
                    err:err
                });
            }
            else{
               const user = new User({
                   _id:new mongoose.Types.ObjectId(),
                   email:req.body.email,
                   password:hash
               });
               user.save()
               .then(result=>{
                   console.log(result)
                   res.status(201).json({
                       message:"User has been created",
                       result:result
                   });
               })
               .catch(err=>{
                   console.log(err)
                   res.status(500).json({
                       error:err
                   });
               })
            }
        })

     }
 })
});


route.post('/login',(req,res,next)=>{
    User.find({email:req.body.email})
    .exec()
    .then(user=>{
        if(user.length<1){
            return res.status(401).json({
                message:"Auth failed"
            });
        }
        bcrypt.compare(req.body.password,user[0].password,(err,result)=>{
            if(err){
                return res.status(401).json({
                    message:"Auth failed"
                }); 
            }
           if(result){
            const token = jwt.sign(
               {
                email:user[0].email,
                userId:user[0]._id
               },
               'secret', { expiresIn: '1h' }
            );
            
            return res.status(200).json({
                message:"Auth Successful",
                token:token
            });
           }
           res.status(401).json({
            message:"Auth failed"
        });
        });
    })
    .catch(err=>{
        console.log(err)
        res.status(500).json({
            error:err
        });
    })
})

route.delete('/:userId',(req,res,next)=>{
    User.remove({_id:req.params.userId})
    .exec()
    .then(result=>{
        res.status(200).json({
            message:"User Deleted"
        });
    })
    .catch(err=>{
        res.status(500).json({
            err:err
        });
    })
})

module.exports = route