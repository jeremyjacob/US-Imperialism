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

	document.addEventListener('keydown', (event) => {
		if (event.key == 'Escape') selected.set('')
	})

	onMount(() => {
		// svgPanZoom('svg')
		const x = document.querySelector('#root')
		// const zoomer = panzoom(container, {
		// 	zoomSpeed: 0.1,
		// 	maxZoom: 5,
		// 	minZoom: 1,
		// })

		// zoomer.zoomTo(1000, 0, 1.2)

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
			if (value)
				container.querySelector('.' + value)?.classList.add('selected')
			else
				container
					.querySelector('region.selected')
					?.classList.remove('selected')

			container.querySelectorAll('.region').forEach((_country) => {
				const country = _country as SVGElement
				let name = Array.from(country.classList).find(
					(e) => e != 'region'
				)
				country.addEventListener('click', (event) => {
					selected.set(name as any)
				})
			})
		})

		document.addEventListener('click', (event) => {
			const element = event.target as SVGElement
			if (
				element.parentElement.classList.contains('container') ||
				element.parentElement.classList.contains('region') ||
				element.classList.contains('region')
			)
				return
			console.log(element)
			selected.set('')
		})
	})
</script>

<div class="map-container" bind:this={container}>
	{@html map}
</div>

<style lang="scss">
	:global(.country-container > *) {
		transform: translate3d(0, 0.01px, 0);
		backface-visibility: hidden;
		stroke: hsl(49, 40%, 87%);
		fill: hsla(49, 40%, 87%, 0.2);
	}

	:global(.region) {
		fill: hsla(49, 40%, 87%, 1);
		cursor: pointer;
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
		pointer-events: none;
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
		transform: scale(1.2);
		top: 0em;
		left: -10em;
		width: 100vw;
		height: 100vh;
	}
</style>
