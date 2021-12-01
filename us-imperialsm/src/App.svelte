<script lang="ts">
	import Map from './lib/Map.svelte'
	import Ribbon from './lib/Ribbon.svelte'
</script>

<main>
	<Map />
	<!-- <Ribbon /> -->
</main>

<style>
	:root {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
			Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}

	h1 {
		position: absolute;
		top: -0.2em;
		width: 100%;
		text-align: center;
	}
</style>
