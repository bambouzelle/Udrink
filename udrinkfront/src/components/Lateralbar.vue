<!-- eslint-disable vue/multi-word-component-names -->
<template>
<div>
 <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
    Button with data-bs-target
  </button>
<div class="collapse" id="collapseExample">
  <div class="card card-body">
    Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
  </div>
</div>
</div>
</template>

<script>
export default {
  name: "NavBar"
};
</script>

<style>
</style>