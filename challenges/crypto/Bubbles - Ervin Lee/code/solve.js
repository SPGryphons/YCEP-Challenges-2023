// Default solution will be in JavaScript (Node.js).
var arr = [
	65, 66, 74, 122, 106, 110, 48, 95, 114, 79, 77, 122,
	58, 48, 42, 118, 101, 53, 122, 109, 39, 104, 122, 83,
	110, 100, 64, 34, 94, 85, 102, 42, 38, 49, 61, 81,
	69, 119, 107, 40, 54, 104, 107, 121, 99, 63, 60, 105,
	101, 53, 108, 85, 89, 100, 51, 67, 70, 120, 98, 103,
	99, 70, 52, 71, 82, 42, 71, 56, 122, 78, 43, 100,
	88, 85, 84, 85, 63, 80, 69, 103, 86, 79, 64, 101,
	38, 75, 52, 73, 68, 35, 49, 81, 82, 43, 35, 90,
	83, 89, 92, 79
]

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
