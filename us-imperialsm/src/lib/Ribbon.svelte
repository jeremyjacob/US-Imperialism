<script lang="ts">
</script>

<div class="container">
	<span class="left">{'American Imperialism '.repeat(6)}</span>
	<span class="right">{'American Imperialism '.repeat(6)}</span>
	<span class="top">{'American Imperialism '.repeat(11)}</span>
	<span class="bottom">{'American Imperialism '.repeat(11)}</span>
</div>

<style lang="scss">
	.container {
		height: 100vh;
		width: 100vw;
		position: absolute;
		top: 0;
		left: 0;
		pointer-events: none;

		span {
			display: inline-block;
			white-space: nowrap;
			overflow: hidden;
			text-transform: uppercase;
			position: absolute;
			background-color: black;
			/* padding: 0.1em 0em; */
			padding-bottom: 0.1em;
			font-size: 1.2em;
		}

		.left {
			bottom: -0.3em;
			left: 0.48em;
			transform-origin: 0;
			transform: rotate(-90deg);
		}
		.right {
			bottom: 0em;
			right: 1.2em;
			transform-origin: 100% 100%;
			transform: rotate(90deg);
		}

		.bottom {
			bottom: 0em;
		}
	}
</style>
