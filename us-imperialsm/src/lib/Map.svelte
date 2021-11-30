<script lang="ts">
	import map from '../assets/map.svg?raw'
	import { tweened } from 'svelte/motion'
	import { cubicOut } from 'svelte/easing'

	let opts = {
		duration: 500,
		easing: cubicOut,
	}

	let scale = tweened(1, opts)
	let x = tweened(0, opts)
	let y = tweened(0, opts)

	let mousePrev = { x: 0, y: 0 }
	let mapPrev = { x: 0, y: 0 }

	document.addEventListener('mousedown', (event) => {
		document.addEventListener('mousemove', move)
		mousePrev.x = event.x
		mousePrev.y = event.y
		mapPrev.x = $x
		mapPrev.y = $y
	})
	document.addEventListener('mouseup', (event) =>
		document.removeEventListener('mousemove', move)
	)

	function move(event: MouseEvent) {
		const _x = mousePrev.x - event.x
		const _y = mousePrev.y - event.y

		x.set(mapPrev.x - _x * 0.8)
		y.set(mapPrev.y - _y * 0.8)
	}

	window.addEventListener('mousewheel', (event: any) => {
		const newScale = $scale + event.deltaY * 0.01
		if (newScale <= 1) {
			scale.set(1)
			x.set(0)
			y.set(0)
		} else if (newScale >= 5) scale.set(5)
		else scale.set(newScale)
	})
</script>

<div class="container" style="--x:{$x}px; --y:{$y}px; --scale:{$scale};">
	{@html map}
</div>

<style lang="scss">
	:global(.region) {
		transition: all 0.4s cubic-bezier(0.33, 1, 0.68, 1);
		transform: translate3d(0, 0.01px, 0);
		backface-visibility: hidden;

		&:hover {
			fill: red;
			transform: translate3d(0, -5px, 0);
		}
	}

	:global(svg) {
	}

	.container {
		transform: scale(var(--scale)) translate(var(--x), var(--y))
			translate3d(0px, 1px, 0px);
		backface-visibility: hidden;
		margin-top: -0.4em;
		cursor: grab;

		&:active {
			cursor: grabbing;
		}
	}
</style>
