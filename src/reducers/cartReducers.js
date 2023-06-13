import { CART_ADD_ITEM } from '../constants/cartConstants'




export const cartReducer = (state={cartItems:[]}, action) => {
    switch(action.type){
        case CART_ADD_ITEM:
            const item = action.payload
            const existItem = state.cartItems.find(x => x.product === item.product)
            if(existItem){
                return{
                    ...state,
                    cartItems: state.cartItems.map(x =>
                        x.product === existItem.product ? item : x //If it matches with the exist item, we will replace is with the new item, if it doesnt we return x
                        )
                }

            }else{
                return{
                    ...state, //Else we return the original state
                    cartItems:[...state.cartItems, item]
                }
            }
        default:
            return state
    }
}