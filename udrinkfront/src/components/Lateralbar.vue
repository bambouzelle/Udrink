<!-- eslint-disable vue/multi-word-component-names -->
<template>
	<div>
		<div class="container-fluid">
			<div class="row">
				<div class="col px-0">
					<Transition name="slide">
						<div v-show="test" id="lateralBar" class="card card-body lateralBar border-top rounded-0"
							style="width: 100%;">
							<div class="row">
								<div class="col px-0">
									<div class="textMenu">Mes ingrédients</div>
								</div>
								<div class="col px-0">
									<img src="../assets/left-arrow.svg" style="max-height: 3em;" @click="toggleLateralBar"
										type="button">
								</div>
							</div>
						</div>
					</Transition>
				</div>
			</div>
			<div class="col px-0">
				<div v-show="!test">
					<button @click="toggleLateralBar" class="bouton" type="button" style="margin-top:1em;">
						Mes ingrédients
					</button>
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
	mounted() {
		console.log(this.barHeight)
		var lateralBar = document.getElementById("lateralBar")
		lateralBar.style.height = this.barHeight + "px";
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
	transform: translateX(-200px);
} 
</style>