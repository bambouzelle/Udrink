<!-- eslint-disable vue/multi-word-component-names -->
<template>
	<div class="container-grid border-top rounded-0">
		<Transition name="slide" id="panel">
			<div v-if="lateralBarShowed" class="lateralBar panelGrid">
				<div id="titrePanel" class="textMenu">Mes ingrédients</div>
				<div id="contentPanel" class="textMenu"> pas d'ingrédients !</div>
			</div>
		</Transition>

		<div ref="buttonBar" class="lateralBar" id="button">
			<img ref="image" v-show="lateralBarShowed" src="../assets/left-arrow.svg" style="max-height: 3em;"
				@click="toggleLateralBar" type="button">

			<img v-show="!lateralBarShowed" src="../assets/ingredients.png" style="max-height: 3em;" @click="toggleLateralBar"
				type="button">

		</div>

	</div>
</template>

<script>
export default {
	name: "NavBar",
	data() {
		return {
			lateralBarShowed: false,
			buttonOffset: 0,
			buttonWidth: 48,
		}
	},
	created() {
		this.lateralBarShowed = false
	},
	mounted() {
		this.buttonOffset = this.$refs.buttonBar.getBoundingClientRect().left;
		this.$refs.buttonBar.style.transition = '0s'
		this.$refs.buttonBar.style.transform = 'translate(-' + this.buttonOffset + 'px)';
		window.onresize = () => {
			this.$router.go(0)
		}
	},
	methods: {
		toggleLateralBar() {
			this.$refs.buttonBar.style.transition = 'all 0.3s ease-in-out'
			if (this.$refs.image.width != 0) {
				this.$refs.buttonBar.width = this.$refs.image.width
			}
			this.lateralBarShowed = !this.lateralBarShowed
			if (this.lateralBarShowed) {
				this.$refs.buttonBar.style.transform = "translate(+" + 0 + "px)";
			}

			else {
				this.$refs.buttonBar.style.transform = "translate(-" + this.buttonOffset + "px)";
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

.panelGrid {
	display: grid;
	grid-template-rows: 1fr 30fr;
}

#titrePanel {
	grid-row-start: 1;
	grid-row-end: 2;
}

#panel {
	grid-column-start: 1;
	grid-column-end: 2;
	grid-row-start: 1;
	grid-row-end: 3;
}

#contentPanel {
	grid-row-start: 2;
	grid-row-end: 3;
}

#button {
	grid-column-start: 2;
	grid-column-end: 3;
	grid-row-start: 1;
	grid-row-end: 2;
	border-start-end-radius: 55%;
	border-end-end-radius: 55%;
	transition: all 0.3s ease-in-out;
	width: 46px;
}

.lateralBar {
	background-color: var(--main-black);
	box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px;
}

.slide-enter-active,
.slide-leave-active {
	transition: all 0.3s ease-in-out;
}

.slide-enter-from,
.slide-leave-to {
	transform: translateX(-100%);
}
</style>