import java.io.File
import java.util.*

fun main() {
    println("Answer 1: " + solve1("src/main/resources/input.txt"));
    println("Answer 2: " + solve2("src/main/resources/input.txt"));
}

fun solve1(fileName: String): Int {
    var ans = 0
    var prev = Integer.MAX_VALUE
    var curr: Int
    File(fileName).forEachLine {
        curr = Integer.valueOf(it);
        if (curr > prev) {
            ans++
        }
        prev = curr
    }
    return ans
}

fun sum(arr: Queue<Int>): Int {
    var ans = 0
    arr.forEach { ans += it }
    return ans
}

fun solve2(fileName: String): Int {
    var ans = 0
    var prev = Integer.MAX_VALUE
    val array: Queue<Int> = LinkedList();
    array.add(prev)
    array.add(prev)
    array.add(prev)

    var curr: Int
    File(fileName).forEachLine {
        array.poll()
        curr = Integer.valueOf(it)
        array.add(curr)
        assert(array.size == 3)
        if (sum(array) > prev) {
            ans++
        }
        prev = sum(array)
        println(array + " " + ans)
    }

    return ans
}