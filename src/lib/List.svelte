<script lang="ts">
	import { selected } from './store'
</script>

<div class="container">
	<div
		on:click={() => selected.set('china')}
		class:selected={$selected == 'china'}
	>
		China
	</div>
	<div
		on:click={() => selected.set('natives')}
		class:selected={$selected == 'natives'}
	>
		Western Natives
	</div>
	<div
		on:click={() => selected.set('alaska')}
		class:selected={$selected == 'alaska'}
	>
		Alaska
	</div>
	<div
		on:click={() => selected.set('hawaii')}
		class:selected={$selected == 'hawaii'}
	>
		Hawaii
	</div>
	<div
		on:click={() => selected.set('cuba')}
		class:selected={$selected == 'cuba'}
	>
		Cuba
	</div>
	<div
		on:click={() => selected.set('philippines')}
		class:selected={$selected == 'philippines'}
	>
		Philippines
	</div>
	<div
		on:click={() => selected.set('panama')}
		class:selected={$selected == 'panama'}
	>
		Panama
	</div>
	<div
		on:click={() => selected.set('honduras')}
		class:selected={$selected == 'honduras'}
	>
		Honduras & Nicaragua
	</div>
</div>

<style lang="scss">
	.container {
		position: absolute;
		padding: 10em 5em;
		padding-left: 3em;
		top: 13%;
		/* background: linear-gradient(90deg, black 0%, transparent 100%); */
		background: radial-gradient(
				ellipse at left,
				black 0%,
				black 20%,
				transparent 70%
			)
			no-repeat;
		/* background-position-x: -5em; */

		div {
			font-size: 1.3em;
			padding: 0.12em 0;
			transition: all 0.4s cubic-bezier(0.33, 1, 0.68, 1);
			transform-origin: left;
			cursor: pointer;

			&:hover {
				transform: scale(1.2);
				color: rgb(216, 216, 216);
			}

			&.selected {
				color: rgb(221, 92, 92);
				transform: scale(1.2);
			}
		}
	}
</style>
