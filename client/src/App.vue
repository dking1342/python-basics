<template>
  <div class="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <strong>Jackets</strong>
        </router-link>
        <a href="#" aria-label="menu" aria-expanded="false" data-target="navbar-menu" class="navbar-burger" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div class="navbar-start">
        <div class="navbar-item">
          <form action="/search" method="GET">
            <div class="field has-addons">
              <div class="control">
                <input type="text" class="input" placeholder="What are you looking for?" name="query">
              </div>
              <div class="control">
                <button class="button is-success">
                  <span class="icon"><i class="fas fa-search"></i></span>
                </button>
              </div>
            </div>
          </form>
        </div>
      </div>
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/winter" class="navbar-item">Winter</router-link>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light">Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <div class="is-loading-bar has-text-centered" :class="{'is-loading' : $store.state.isLoading }" >
      <div class="lds-dual-ring"></div>
    </div>
    <section class="section">
      <router-view/>
    </section>
    <footer class="footer">
      <p class="has-text-centered">Copyright &copy; 2021</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios"
export default {
  data(){
    return{
      showMobileMenu:false,
      cart:{
        items:[]
      }
    }
  },
  beforeCreate(){
    this.$store.commit('initializeStore')
    const token = this.$store.state.token

    if(token){
      axios.defaults.headers.common["Authorization"] = "Token " + token
    } else {
      axios.defaults.headers.common["Authorization"] = ""
    }
  },
  mounted(){
    this.cart = this.$store.state.cart
  },
  computed:{
    cartTotalLength(){
      if (this.cart.items.length) {
        return this.cart.items.reduce((acc,val) => acc + val.quantity,0)
      } else {
        return 0
      }
    }
  }

}
</script>

<style lang="scss">
@import "../node_modules/bulma";
.lds-dual-right {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content:" ";
  display: block;
  width: 64px;
  height: 64px;
  margin:8px;
  border-radius: 50%;
  border:6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lsd-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg)
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow:hidden;

  -webkit-transition: all 0.3s;
  transition:all 0.3s;

  &.is-loading {
    height: 80px;
  }
}
</style>
