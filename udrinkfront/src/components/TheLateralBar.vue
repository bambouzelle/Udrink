<!-- eslint-disable vue/multi-word-component-names -->
<template>
			<div class="container-grid border-top rounded-0">
						<Transition name="slide" id="panel">
							<div v-if="lateralBarShowed" class ="lateralBar panelGrid">
								<div id="titrePanel" class="textMenu">Mes ingrédients</div>
								<div id="contentPanel" class="textMenu"> pas d'ingrédients !</div>
							</div>
						</Transition>
	
						<img src="../assets/left-arrow.svg" style="max-height: 3em;" @click="toggleLateralBar"
							type="button"
							id="button"
							class="lateralBar"
							>
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
			//const button = document.getElementById('button')
			if (this.lateralBarShowed){
				//button.style.transform = "translate(100%)"
			} 
			else {
				//button.style.transform = "translate(0px)"
			}
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
.container-grid {
	display: grid;
	grid-template-columns: 10fr 3fr;
	grid-template-rows: 1fr 30fr;
	width: 200%;
	z-index: 999;
}

.panelGrid{
	display: grid;
	grid-template-rows: 1fr 30fr;
}

#titrePanel{
	grid-row-start: 1;
	grid-row-end: 2;
}

#panel {
	grid-column-start: 1;
  grid-column-end: 2;
	grid-row-start: 1;
	grid-row-end: 3;
}

#contentPanel{
	grid-row-start: 2;
	grid-row-end: 3;
}

#button {
	grid-column-start: 2;
  grid-column-end: 3;
	grid-row-start: 1;
	grid-row-end: 2;
	border-start-end-radius: 55%;
	border-end-end-radius:55%;
	transform: translateX(-452%);
	transition-delay: 0.25s;
	transition: transform 0.3s ease-in-out;
	position: relative;
}

.buttonLeft{
	transform: translateX(452%);
	transition-delay: 0.25s;
	transition: transform 0.3s ease-in-out;
}

.lateralBar {
	background-color: var(--main-black);
	box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
}

.slide-enter-active,
.slide-leave-active {
	transition: all 0.3s ease-in-out;
}

/* delay leave of parent element */
.slide-leave-active {
	transition-delay: 0.25s;
}

.slide-enter-from,
.slide-leave-to {
	transform: translateX(-100%);
}
</style>