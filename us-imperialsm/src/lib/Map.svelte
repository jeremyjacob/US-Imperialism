<script lang="ts">
	import map from '../assets/map.svg?raw'
	import { tweened } from 'svelte/motion'
	import { cubicOut } from 'svelte/easing'
	// import svgPanZoom from 'svg-pan-zoom'
	import panzoom from 'panzoom'
	import { onMount } from 'svelte'

	let opts = {
		duration: 500,
		easing: cubicOut,
	}

	let container: HTMLDivElement
	let scale = tweened(1, opts)
	let x = tweened(0, opts)
	let y = tweened(0, opts)

	onMount(() => {
		// svgPanZoom('svg')
		const x = document.querySelector('#root')
		const zoomer = panzoom(container, {
			zoomSpeed: 0.15,
			// maxZoom: 5,
			minZoom: 1,
			bounds: true,
			boundsPadding: 0.1,
		})

		// zoomer.smoothZoom(1700, 400, 1.7)

		container.addEventListener('click', (event) => {})
	})
</script>

<div class="container" bind:this={container}>
	{@html map}
</div>

<style lang="scss">
	:global(.country-container > *) {
		transition: all 0.4s cubic-bezier(0.33, 1, 0.68, 1);
		transform: translate3d(0, 0.01px, 0);
		backface-visibility: hidden;
		stroke: hsl(49, 40%, 87%);
		fill: hsla(49, 40%, 87%, 0.2);
	}

	:global(.region) {
		fill: hsla(49, 40%, 87%, 1);

		&:hover.no {
			/* &:global(.selected) { */
			/* fill: red; */
			/* transform: translate3d(0, -5px, 0); */
			transform: translateY(-5px);
		}
	}

	:global(#graticules) {
		stroke: #838383;
	}

	:global(#lines > *) {
		stroke: red;
		stroke-width: 2;
		stroke-dasharray: 4;
		fill: transparent;
	}

	:global(#sphere) {
		stroke: #0e0e0eaf;
		stroke-width: 4;
	}

	.container {
		backface-visibility: hidden;
		/* cursor: grab; */
		position: absolute;
		top: 0;
		left: 0;
		width: 100vw;
		height: 100vh;
	}
</style>
