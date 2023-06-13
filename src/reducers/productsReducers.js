//A reducer is a function that takes in our current state and its going to take an action of what we are going to do to the state
//Takes a state && an action type -> manipulates our state or a certain part of our statem and it returns a new copy into our store
//The reducer is what actually updates our store
import { 
    PRODUCT_LIST_REQUEST,
    PRODUCT_LIST_SUCCESS,
    PRODUCT_LIST_FAIL,

    PRODUCT_DETAILS_REQUEST,
    PRODUCT_DETAILS_SUCCESS,
    PRODUCT_DETAILS_FAIL,
 } from '../constants/productConstants'

export const productListReducer = (state ={products:[]},action) =>{
    switch(action.type){
        case PRODUCT_LIST_REQUEST:
          
            return {loading:true,products:[]}
        case PRODUCT_LIST_SUCCESS:
        
            return {loading:false,products: action.payload}
        case PRODUCT_LIST_FAIL:
       
            return {loading:false,error: action.payload}

        default:
            return state
    }
}

export const productDetailsReducer = (state ={product:{reviews:[]}},action) =>{
    switch(action.type){
        case PRODUCT_DETAILS_REQUEST:
           
            return {loading:true, ...state}
        case PRODUCT_DETAILS_SUCCESS:
       
            return {loading:false,product: action.payload}
        case PRODUCT_DETAILS_FAIL:
   
            return {loading:false,error: action.payload}

        default:
            return state
    }
}
