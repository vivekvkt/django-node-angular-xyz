const express = require('express')

const router =  express.Router();

//handlin incoming get request product api

router.get('/',(req,res,next)=>{
    res.status(200).json({
        message:"product handling get method"
    })
})


router.get('/:productId',(req,res,next)=>{
    productId = req.params.productId

    if (productId=='done'){
        res.status(200).json({
            message:"Getting Product Id",
            id:productId
        })
    }
    else{
        res.status(200).json({
            message:"you nees to pass Id for get Item "
        })
    }

   
})



router.post('/',(req,res,next)=>{
    res.status(200).json({
        message:"product handling Post method"
    })
})


// router.put('/',(req,res,next)=>{
//     res.status(200).json({
//         message:"product handling update method"
//     })
// })


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

// router.patch('/',(req,res,next)=>{
//     res.status(200).json({
//         message:"product handling patch method"
//     })
// })


router.patch('/:productId',(req,res,next)=>{
    productId = req.params.productId

    if (productId=='patch'){
        res.status(200).json({
            message:"Getting Product Id",
            id:productId
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