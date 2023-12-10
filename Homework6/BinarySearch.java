public class BinarySearch {
    public static int binarySearch(int[] array, int target) {
        int left = 0;
        int right = array.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (array[mid] == target) {
                return mid; // Элемент найден, возвращаем индекс
            } else if (array[mid] < target) {
                left = mid + 1; // Искомый элемент в правой половине
            } else {
                right = mid - 1; // Искомый элемент в левой половине
            }
        }

        return -1; // Элемент не найден
    }

    public static void main(String[] args) {
        int[] sortedArray = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int targetElement = 7;

        int result = binarySearch(sortedArray, targetElement);

        if (result != -1) {
            System.out.println("Элемент " + targetElement + " найден по индексу " + result);
        } else {
            System.out.println("Элемент " + targetElement + " не найден в массиве");
        }
    }
}
