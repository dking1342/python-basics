<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in cart.items" :key="item.product.id" >
                            <td>{{ item.product.name }}</td>
                            <td>${{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>{{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <div class="column is-12 box">
                <h2 class="subtitle">Shipping details</h2>
                <p class="has-text-grey mb-4">* All fields are required</p>
                <div class="columns is-multiline">
                    <div class="column is-6">
                        <div class="field">
                            <label for="">First name</label>
                            <div class="control">
                                <input type="text" name="" id="" class="input" v-model="first_name" required>
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Last name</label>
                            <div class="control">
                                <input type="text" name="" id="" class="input" v-model="last_name" required>
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Email</label>
                            <div class="control">
                                <input type="email" name="" id="" class="input" v-model="email" required>
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Phone</label>
                            <div class="control">
                                <input type="tel" name="" id="" class="input" v-model="phone" required>
                            </div>
                        </div>
                    </div>
                    <div class="column is-6">
                        <div class="field">
                            <label for="">Address</label>
                            <div class="control">
                                <input type="text" name="" id="" class="input" v-model="address" required>
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Zipcode</label>
                            <div class="control">
                                <input type="number" min="00001" max="99999" step="1" name="" id="" class="input" v-model="zipcode" required>
                            </div>
                        </div>
                        <div class="field">
                            <label for="">Place</label>
                            <div class="control">
                                <input type="text" name="" id="" class="input" v-model="place" required>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" :key="error" >{{ error }}</p>
                </div>
                <hr>
                <div id="card-element" class="mb-5"></div>
                <template v-if="cartTotalLength">
                    <hr>
                    <button class="button is-dark" @click="submitForm" >Pay with Stripe</button>
                </template>
            </div>   
        </div>
    </div>
</template>

<script>
import axios from "axios"
export default {
    name:"Checkout", 
    data(){
        return{
            cart:{
                items:[]
            },
            stripe:{},
            card:{},
            first_name:"",
            last_name:"",
            email:"",
            phone:"",
            address:"",
            zipcode:"",
            place:"",
            errors:[],
        }
    },
    mounted(){
        document.title = "Checkout | Jackets"
        this.cart = this.$store.state.cart
    },
    methods:{
        getItemTotal(item){
            return item.quantity * item.product.price
        },
        submitForm(){
            this.errors = []
            if(this.first_name === ""){
                this.errors.push("The first name field is missing")
            }
            if(this.last_name === ""){
                this.errors.push("The last name field is missing")
            }
            if(this.email === ""){
                this.errors.push("The email field is missing")
            }
            if(this.phone === ""){
                this.errors.push("The phone field is missing")
            }
            if(this.address === ""){
                this.errors.push("The address field is missing")
            }
            if(this.zipcode === ""){
                this.errors.push("The zipcode field is missing")
            }
            if(this.place === ""){
                this.errors.push("The place field is missing")
            }
        }
    },
    computed:{
        cartTotalLength(){
            return this.cart.items.reduce((acc,val)=>{
                return acc += val.quantity
            },0)
        },
        cartTotalPrice(){
            return this.cart.items.reduce((acc,val)=>{
                return acc += val.product.price * val.quantity
            },0)
        }
    }
}
</script>

<style lang="scss" scoped>

</style>