<script lang="ts">
	import Note from './lib/Note.svelte'
	import List from './lib/List.svelte'
	import Map from './lib/Map.svelte'
	import Ribbon from './lib/Ribbon.svelte'
	import data from './lib/data'
	import { selected } from './lib/store'

	let lastInput = Date.now()
	const input = () => (lastInput = Date.now())

	setInterval(() => {
		if (Date.now() - lastInput > 1000 * 30) selected.set('')
	}, 1000)

	document.addEventListener('keydown', input)
	document.addEventListener('mousemove', input, { passive: true })
</script>

<main>
	<Map />
	<List />
	<Ribbon />
	{#if $selected}
		<Note {...data[$selected]} />
	{/if}
</main>

<style>
	:root {
		font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
			Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
	}
</style>
