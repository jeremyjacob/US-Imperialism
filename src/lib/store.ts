import { writable } from 'svelte/store'

export const selected = writable<
	| 'japan'
	| 'china'
	| 'natives'
	| 'alaska'
	| 'hawaii'
	| 'cuba'
	| 'philippines'
	| 'panama'
	| 'honduras'
	| ''
>('')
