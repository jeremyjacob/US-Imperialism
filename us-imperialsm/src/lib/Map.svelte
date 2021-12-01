<script lang="ts">
	import map from '../assets/map.svg?raw'
	import { tweened } from 'svelte/motion'
	import { cubicOut } from 'svelte/easing'
	// import svgPanZoom from 'svg-pan-zoom'
	// import panzoom from 'panzoom'
	import { onMount } from 'svelte'
	import { selected } from './store'

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
		// const zoomer = panzoom(container, {
		// 	zoomSpeed: 0.1,
		// 	maxZoom: 5,
		// 	minZoom: 1,
		// })

		// zoomer.zoomTo(1000, 0, 1.2)

		container.addEventListener('click', (event) => {})

		selected.subscribe((value) => {
			container?.querySelectorAll('#lines > path').forEach((_line) => {
				const line = _line as SVGPathElement
				if (value) line.classList.remove('selected')
				else line.classList.add('selected')
			})
			container?.querySelectorAll('.region').forEach((country: any) => {
				if (value) country.classList.remove('selected')
			})
			container.querySelector('.line-' + value)?.classList.add('selected')
			value &&
				container.querySelector('.' + value)?.classList.add('selected')
		})

		container.querySelectorAll('.region').forEach((_country) => {
			const country = _country as SVGElement
			let name = Array.from(country.classList).find((e) => e != 'region')
			country.addEventListener('click', (event) => {
				selected.set(name as any)
			})
		})
	})
</script>

<div class="map-container" bind:this={container}>
	{@html map}
</div>

<style lang="scss">
	:global(.country-container > *) {
		transition: all 0s cubic-bezier(0.33, 1, 0.68, 1);
		transform: translate3d(0, 0.01px, 0);
		backface-visibility: hidden;
		stroke: hsl(49, 40%, 87%);
		fill: hsla(49, 40%, 87%, 0.2);
	}

	:global(.region) {
		fill: hsla(49, 40%, 87%, 1);
		cursor: pointer;

		&:hover.no {
			/* &:global(.selected) { */
			/* fill: red; */
			/* transform: translate3d(0, -5px, 0); */
			transform: translateY(-5px);
		}
	}
	:global(.region.selected) {
		fill: rgb(175, 18, 18);
	}

	:global(#graticules) {
		stroke: #838383;
	}

	@keyframes dash {
		to {
			stroke-dashoffset: -130000em;
		}
	}

	:global(#lines > *) {
		stroke: rgb(221, 92, 92);
		stroke-width: 3;
		stroke-dasharray: 4;
		fill: transparent;
		stroke-dashoffset: 0;
		visibility: hidden;
		animation: dash 216000s linear forwards;
	}
	:global(#lines > .selected) {
		visibility: visible;
	}

	:global(#sphere) {
		stroke: #0e0e0eaf;
		stroke-width: 4;
	}

	.map-container {
		backface-visibility: hidden;
		/* cursor: grab; */
		position: absolute;
		top: 10em;
		transform: scale(1.2);
		left: 18em;
		width: 100vw;
		height: 100vh;
	}
</style>
