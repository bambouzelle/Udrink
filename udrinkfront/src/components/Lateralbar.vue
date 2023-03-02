<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <div class="col px-0">
          <div class="collapse collapse-horizontal" id="collapseWidthExample">
            <div class="card card-body lateralBar" style="width: 200%; height: 50em;">
              <div class="row">
                <div class="col px-0">
                  <div class="textMenu">Mes ingrédients</div>
                </div>
                <div class="col px-0">
                  <img src="../assets/left-arrow.svg" style="max-height: 3em;" @click="toggleLateralBar" type="button"
                    data-bs-toggle="collapse" data-bs-target="#collapseWidthExample" aria-expanded="false"
                    aria-controls="collapseWidthExample">
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col px-0">
          <div v-show="!test">
            <button @click="toggleLateralBar" class="btn btn-primary" type="button" data-bs-toggle="collapse"
              data-bs-target="#collapseWidthExample" aria-expanded="false" aria-controls="collapseWidthExample">
              Mes ingrédients
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  data() {
    return {
      lateralBarShowed: false
    }
  },
  created() {
    this.lateralBarShowed = false
  },
  methods: {
    toggleLateralBar() {
      this.lateralBarShowed = !this.lateralBarShowed
    }
  },
  computed: {
    test() {
      return this.lateralBarShowed
    }
  }
};
</script>

<style>
  .lateralBar{
    background-color:#001e1f ;
  }
</style>