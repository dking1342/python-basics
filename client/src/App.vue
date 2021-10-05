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
      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active':showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/summer" class="navbar-item">Summer</router-link>
          <router-link to="/winter" class="navbar-item">Winter</router-link>
          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log in</router-link>
              <router-link to="/cart" class="button is-success">
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart ({{ cartTotalLength }})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>
    <section class="section">
      <router-view/>
    </section>
    <footer class="footer">
      <p class="has-text-centered">Copyright &copy; 2021</p>
    </footer>
  </div>
</template>

<script>
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
</style>
