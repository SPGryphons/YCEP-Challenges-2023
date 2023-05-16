// Default solution will be in JavaScript (Node.js).
var arr = [];
for (var i = 0; i < 100; i++) {
	arr.push(Math.floor(Math.random() * 127) + 31);
}

console.log(arr);

var iteration_number = 55;

function swap(array, xp, yp) {
	var temp = arr[xp];
	arr[xp] = arr[yp];
	arr[yp] = temp;
}

function sortBubbles(arr, n) {
	var i, j;
	for (i = 0; i < n - 1; i++) {
		for (j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				swap(arr, j, j + 1);
			}
		}
		console.log("Iteration " + (i + 1) + ": ");
		console.log(arr);
		if (i + 1 == iteration_number) {
			console.log("Iteration " + (i + 1) + ": ");
			console.log(arr);
			return arr;
		}
	}
}

function printArray(arr, size) {
	var i;
	for (i = 0; i < size; i++) {
		console.log(arr[i]);
	}
}

var n = arr.length;
var select_array = sortBubbles(arr, n);
var flag_value = "";
for (var i = 0; i < select_array.length; i++) {
	flag_value += String.fromCharCode(select_array[i]);
}

console.log(flag_value);
