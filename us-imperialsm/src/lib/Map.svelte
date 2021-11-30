<script lang="ts">
	import map from '../assets/map.svg?raw'
</script>

<div class="container">
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
</style>
