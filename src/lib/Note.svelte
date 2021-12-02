<script lang="ts">
	import { selected } from './store'

	export let coords = [50, 50]
	export let height: number
	export let body: string
	export let _body: string
	export let country: string
	export let _country: string

	function fade(node, { duration }) {
		return {
			duration,
			css: (t) => {
				return `
					opacity: ${t * 0.5 + 0.5};`
			},
		}
	}

	$: {
		setTimeout(() => (_body = body), 200)
		setTimeout(() => (_country = country), 200)
	}
</script>

<div
	class="card"
	style="--x:{coords[0]}px; --y:{coords[1]}px; --height:{height}px;"
>
	{#key $selected}
		<h1 transition:fade={{ duration: 200 }}>
			{country}
		</h1>
		<p transition:fade={{ duration: 200 }}>
			{body}
		</p>
	{/key}
</div>

<style lang="scss">
	.card {
		width: 25em;
		height: var(--height);
		position: absolute;
		top: var(--y);
		left: var(--x);
		background: hsla(0, 0%, 0%, 0.6);
		backdrop-filter: blur(7px);
		padding: 0 2em;
		padding-bottom: 0.3em;
		transition: all 0.65s cubic-bezier(0.32, 0.28, 0.44, 1.06);
		pointer-events: none;
		overflow: hidden;
	}

	p {
	}

	h1 {
		margin-bottom: 0em;
		font-size: 1.9em;
	}
</style>
