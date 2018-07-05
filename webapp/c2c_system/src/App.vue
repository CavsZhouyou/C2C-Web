<template>
    <div id="app">
        <transition name="fade" enter-active-class="fadeInLeft" leave-active-class="fadeOutRight" mode="out-in">
            <router-view/>
        </transition>
    </div>
</template>

<style lang="scss">
@import "./css/normalize";

#app {
    font-family: "Avenir", Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
}
#nav {
    padding: 30px;
    a {
        font-weight: bold;
        color: #2c3e50;
        &.router-link-exact-active {
            color: #42b983;
        }
    }
}
</style>
