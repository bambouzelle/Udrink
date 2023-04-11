<template>
	<div class="card mb-3 px-0" style="max-width: 100%;">
		<div class="row g-0">
			<h5 class="card-header">{{ ingredient.name }}</h5>
		</div>
		<div class="row g-0">
			<!--<div class="col-md-4">
				<div class="card px-0 rounded-0">
					<img src="../assets/cocktailPNG37.png" class="img-fluid rounded-start" alt="..."
						style="max-height: 2em;">
				</div>

			</div>-->
			<div class="col-md-9">
				<div class="card px-0 border-top-0 border-start-0 border-bottom-0 rounded-0">
					<div class="card-body">
					</div>
				</div>
			</div>
			<div class="col-md-3">
				<div class="card px-0 rounded-0 border-0">
					<div class="card-body">
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name:"IngredientCard",
	props:["ingredient"],
}
</script>

<style></style>