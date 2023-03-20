<template>
	<div>
		<input class="searchBar" type="text" placeholder="Ingrédient..." v-model="searchQuery" />
	</div>
</template>

<script>
export default {
	name: "SearchBar",
	data(){
		return{
			searchQuery:""
		}
	}

}
</script>

<style>
.searchBar {
	border-radius: 30px;
	box-shadow: var(--main-purple) 4px 4px 0 0;
}
</style>