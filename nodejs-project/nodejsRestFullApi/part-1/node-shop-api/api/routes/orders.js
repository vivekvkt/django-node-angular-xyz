const express = require('express')

const router =  express.Router();

router.get('/',(req,res,next)=>{
    res.status(200).json({
        message:"Order handling get method"
    })
})


router.get('/:orderId',(req,res,next)=>{
    orderId = req.params.orderId

    if (orderId=='done'){
        res.status(200).json({
            message:"Getting OrderId Id",
            id:orderId
        })
    }
    else{
        res.status(200).json({
            message:"you nees to pass Id for get Item "
        })
    }

   
})



router.post('/',(req,res,next)=>{
    res.status(201).json({
        message:"orderId handling Post method"
    })
})


// router.put('/',(req,res,next)=>{
//     res.status(200).json({
//         message:"product handling update method"
//     })
// })


router.put('/:orderId',(req,res,next)=>{
    orderId = req.params.orderId

    if (orderId=='update'){
        res.status(200).json({
            message:"Getting orderId Id",
            id:orderId
        })
    }
    else{
        res.status(200).json({
            message:"you nees to pass Id for update"
        })
    }

   
})

// router.patch('/',(req,res,next)=>{
//     res.status(200).json({
//         message:"product handling patch method"
//     })
// })


router.patch('/:orderId',(req,res,next)=>{
    orderId = req.params.orderId

    if (orderId=='patch'){
        res.status(200).json({
            message:"Getting orderId Id",
            id:orderId
        })
    }
    else{
        res.status(200).json({
            message:"you nees to pass Id for Patch Item"
        })
    }

   
})


// router.delete('/',(req,res,next)=>{
//     res.status(200).json({
//         message:"product handling delete method"
//     })
// })


router.delete('/:productId',(req,res,next)=>{
    productId = req.params.productId

    if (productId=='delete'){
        res.status(200).json({
            message:"Getting Product Id",
            id:productId
        })
    }
    else{
        res.status(200).json({
            message:"you nees to pass Id for Delete Item"
        })
    }

   
})

module.exports = router;