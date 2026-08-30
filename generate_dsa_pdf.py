"""
Generate a comprehensive DSA Learning PDF - Basic to Advanced
Includes: Theory, Concepts, Examples, Visual Explanations, Practice Problems
"""

from fpdf import FPDF

class DSAGuide(FPDF):
    def __init__(self):
        super().__init__()
        self.set_auto_page_break(auto=True, margin=20)

    def header(self):
        if self.page_no() > 1:
            self.set_font("Helvetica", "I", 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 8, "DSA Learning Guide - Basic to Advanced", align="C")
            self.ln(5)
            self.set_draw_color(200, 200, 200)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def chapter_title(self, title, level=1):
        if level == 1:
            self.set_font("Helvetica", "B", 18)
            self.set_text_color(30, 60, 120)
            self.cell(0, 12, title, new_x="LMARGIN", new_y="NEXT")
            self.set_draw_color(30, 60, 120)
            self.set_line_width(0.8)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(6)
        elif level == 2:
            self.set_font("Helvetica", "B", 14)
            self.set_text_color(50, 90, 160)
            self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
            self.ln(3)
        elif level == 3:
            self.set_font("Helvetica", "B", 12)
            self.set_text_color(70, 110, 180)
            self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
            self.ln(2)

    def section_text(self, text):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5.5, text)
        self.ln(3)

    def key_concept(self, title, text):
        self.set_fill_color(230, 240, 255)
        self.set_draw_color(30, 60, 120)
        self.set_font("Helvetica", "B", 10)
        self.set_text_color(30, 60, 120)
        x = self.get_x()
        y = self.get_y()
        # Calculate height needed
        self.set_font("Helvetica", "B", 10)
        w = self.get_string_width(title) + 6
        self.rect(x, y, 190, 7, style="DF")
        self.cell(190, 7, title)
        self.ln(8)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(190, 5.5, text)
        self.ln(4)

    def code_block(self, code):
        self.set_fill_color(40, 44, 52)
        self.set_font("Courier", "", 9)
        self.set_text_color(171, 178, 191)
        lines = code.strip().split("\n")
        h = len(lines) * 5 + 6
        x = self.get_x()
        y = self.get_y()
        if y + h > 270:
            self.add_page()
            y = self.get_y()
        self.rect(10, y, 190, h, style="DF")
        self.ln(3)
        for line in lines:
            self.cell(5, 5, "")
            self.set_text_color(198, 120, 221)
            # Simple syntax highlighting for keywords
            self.set_text_color(171, 178, 191)
            self.cell(0, 5, line, new_x="LMARGIN", new_y="NEXT")
            self.set_x(15)
        self.ln(4)

    def table_header(self, headers, widths):
        self.set_font("Helvetica", "B", 9)
        self.set_fill_color(30, 60, 120)
        self.set_text_color(255, 255, 255)
        for i, header in enumerate(headers):
            self.cell(widths[i], 7, header, border=1, fill=True, align="C")
        self.ln()

    def table_row(self, cells, widths, fill=False):
        self.set_font("Helvetica", "", 9)
        self.set_text_color(40, 40, 40)
        if fill:
            self.set_fill_color(240, 245, 255)
        for i, cell in enumerate(cells):
            self.cell(widths[i], 6, cell, border=1, fill=fill, align="C")
        self.ln()

    def visual_box(self, text, fill_color=(230, 240, 255)):
        self.set_fill_color(*fill_color)
        self.set_draw_color(30, 60, 120)
        self.set_font("Courier", "", 9)
        self.set_text_color(30, 30, 30)
        lines = text.strip().split("\n")
        max_w = max(len(l) for l in lines) * 2.5 + 10
        h = len(lines) * 5 + 6
        if max_w > 190:
            max_w = 190
        x = self.get_x()
        y = self.get_y()
        if y + h > 270:
            self.add_page()
        self.rect(x, y, max_w, h, style="DF")
        self.ln(3)
        for line in lines:
            self.cell(5, 5, "")
            self.cell(0, 5, line, new_x="LMARGIN", new_y="NEXT")
            self.set_x(x + 5)
        self.ln(4)

    def practice_problem(self, num, title, difficulty, statement, hints=""):
        colors = {"Easy": (76, 175, 80), "Medium": (255, 152, 0), "Hard": (244, 67, 54)}
        r, g, b = colors.get(difficulty, (100, 100, 100))
        self.set_fill_color(250, 250, 250)
        self.set_draw_color(200, 200, 200)
        y_start = self.get_y()
        if y_start + 40 > 270:
            self.add_page()

        self.set_font("Helvetica", "B", 10)
        self.set_text_color(40, 40, 40)
        self.cell(150, 7, f"Problem {num}: {title}")
        # Difficulty badge
        self.set_fill_color(r, g, b)
        self.set_text_color(255, 255, 255)
        self.set_font("Helvetica", "B", 8)
        self.cell(30, 7, difficulty, fill=True, align="C")
        self.ln(8)

        self.set_font("Helvetica", "", 9)
        self.set_text_color(60, 60, 60)
        self.multi_cell(190, 5, statement)

        if hints:
            self.set_font("Helvetica", "I", 9)
            self.set_text_color(100, 100, 100)
            self.multi_cell(190, 5, f"Hint: {hints}")
        self.ln(4)


def build_pdf():
    pdf = DSAGuide()
    pdf.alias_nb_pages()
    pdf.set_title("DSA Learning Guide - Basic to Advanced")
    pdf.set_author("Claude Code")

    # ========== COVER PAGE ==========
    pdf.add_page()
    pdf.ln(50)
    pdf.set_font("Helvetica", "B", 32)
    pdf.set_text_color(30, 60, 120)
    pdf.cell(0, 15, "Data Structures &", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 15, "Algorithms", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)
    pdf.set_font("Helvetica", "", 16)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "A Comprehensive Learning Guide", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 10, "Basic to Advanced", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(10)
    pdf.set_draw_color(30, 60, 120)
    pdf.set_line_width(1)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(15)
    pdf.set_font("Helvetica", "", 11)
    pdf.set_text_color(100, 100, 100)
    topics = [
        "Arrays | Linked Lists | Stacks | Queues",
        "Trees | Graphs | Hash Tables | Heaps",
        "Sorting | Searching | Dynamic Programming",
        "Greedy Algorithms | Backtracking",
        "Practice Problems with Solutions"
    ]
    for t in topics:
        pdf.cell(0, 7, t, align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(20)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(150, 150, 150)
    pdf.cell(0, 7, "Theory | Concepts | Examples | Visual Explanations", align="C", new_x="LMARGIN", new_y="NEXT")

    # ========== TABLE OF CONTENTS ==========
    pdf.add_page()
    pdf.chapter_title("Table of Contents")
    toc_items = [
        ("1.", "Introduction to DSA", 3),
        ("2.", "Complexity Analysis", 3),
        ("3.", "Arrays", 5),
        ("4.", "Strings", 8),
        ("5.", "Linked Lists", 10),
        ("6.", "Stacks", 13),
        ("7.", "Queues", 15),
        ("8.", "Hash Tables (Hashing)", 17),
        ("9.", "Trees", 20),
        ("10.", "Binary Search Trees (BST)", 23),
        ("11.", "Heaps & Priority Queues", 25),
        ("12.", "Graphs", 27),
        ("13.", "Graph Algorithms", 30),
        ("14.", "Sorting Algorithms", 33),
        ("15.", "Searching Algorithms", 37),
        ("16.", "Dynamic Programming", 39),
        ("17.", "Greedy Algorithms", 43),
        ("18.", "Backtracking", 45),
        ("19.", "Trie (Prefix Tree)", 47),
        ("20.", "Union-Find (Disjoint Set)", 48),
        ("21.", "Practice Problems Collection", 50),
    ]
    pdf.set_font("Helvetica", "", 11)
    for num, title, pg in toc_items:
        pdf.set_text_color(40, 40, 40)
        pdf.cell(10, 7, num)
        pdf.cell(140, 7, title)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 7, str(pg), align="R", new_x="LMARGIN", new_y="NEXT")

    # ========== CHAPTER 1: INTRODUCTION ==========
    pdf.add_page()
    pdf.chapter_title("1. Introduction to Data Structures & Algorithms")

    pdf.section_text(
        "Data Structures and Algorithms (DSA) form the backbone of computer science and software engineering. "
        "They are essential for writing efficient, optimized, and scalable code."
    )

    pdf.chapter_title("What is a Data Structure?", level=2)
    pdf.section_text(
        "A data structure is a way of organizing, storing, and managing data in a computer so that it can be "
        "accessed and modified efficiently. Different data structures are suited for different kinds of tasks, "
        "and some are highly specialized for specific purposes."
    )

    pdf.chapter_title("What is an Algorithm?", level=2)
    pdf.section_text(
        "An algorithm is a step-by-step procedure or set of rules to be followed in calculations or "
        "other problem-solving operations. A good algorithm is efficient, clear, and generalizable."
    )

    pdf.chapter_title("Why Learn DSA?", level=2)
    pdf.section_text(
        "1. Technical Interviews: DSA is the most tested topic in coding interviews at top tech companies.\n"
        "2. Problem Solving: Develops analytical and logical thinking.\n"
        "3. Efficiency: Understanding DSA helps write code that runs faster and uses less memory.\n"
        "4. Foundation: Essential for advanced topics like system design, databases, and OS.\n"
        "5. Career Growth: Opens doors to better job opportunities and higher salaries."
    )

    pdf.chapter_title("Classification of Data Structures", level=2)
    pdf.visual_box(
        "             Data Structures\n"
        "            /             \\\n"
        "     Linear            Non-Linear\n"
        "    /   |   \\          /    |    \\\n"
        "Array  LL  Stack    Tree  Graph  Heap\n"
        "       |    |\n"
        "      Queue Hash\n"
        "       |  Table\n"
        "     Deque"
    )

    pdf.chapter_title("Classification of Algorithms", level=2)
    pdf.visual_box(
        "              Algorithms\n"
        "            /     |      \\\n"
        "     Sorting  Searching  Graph\n"
        "    / | | \\       |      / | \\\n"
        "  B  S  M  Q    Linear BFS DFS\n"
        "  u  e  e  u   Binary\n"
        "  b  l  r  i   Search\n"
        "  b  e  g\n"
        "  l  c  o\n"
        "  e  t  r\n"
        "     i\n"
        "     o\n"
        "     n"
    )

    # ========== CHAPTER 2: COMPLEXITY ANALYSIS ==========
    pdf.add_page()
    pdf.chapter_title("2. Complexity Analysis")

    pdf.section_text(
        "Complexity analysis helps us understand how the runtime or memory usage of an algorithm grows "
        "as the input size grows. This is fundamental to writing efficient code."
    )

    pdf.chapter_title("Time Complexity", level=2)
    pdf.section_text(
        "Time complexity measures the amount of time an algorithm takes to complete as a function of the "
        "input size. We use Big O notation to describe the upper bound of the growth rate."
    )

    pdf.chapter_title("Common Time Complexities", level=2)

    headers = ["Complexity", "Name", "Example"]
    widths = [30, 40, 120]
    pdf.table_header(headers, widths)
    rows = [
        ["O(1)", "Constant", "Array access by index"],
        ["O(log n)", "Logarithmic", "Binary search"],
        ["O(n)", "Linear", "Linear search, single loop"],
        ["O(n log n)", "Linearithmic", "Merge sort, Quick sort (avg)"],
        ["O(n^2)", "Quadratic", "Bubble sort, nested loops"],
        ["O(n^3)", "Cubic", "Matrix multiplication"],
        ["O(2^n)", "Exponential", "Subset generation"],
        ["O(n!)", "Factorial", "Permutation generation"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Visual Comparison of Growth Rates", level=2)
    pdf.visual_box(
        "n     | O(1) | O(logn)| O(n) | O(nlogn)| O(n^2) | O(2^n)\n"
        "------+-------+--------+------+---------+--------+-------\n"
        "  1   |   1   |   0    |   1  |    0    |    1   |    2\n"
        "  4   |   1   |   2    |   4  |    8    |   16   |   16\n"
        "  8   |   1   |   3    |   8  |   24    |   64   |  256\n"
        " 16   |   1   |   4    |  16  |   64    |  256   | 65536\n"
        " 32   |   1   |   5    |  32  |  160    | 1024   |  ~4B\n"
        "100   |   1   |   7    | 100  |  700    | 10000  | huge"
    )

    pdf.chapter_title("Space Complexity", level=2)
    pdf.section_text(
        "Space complexity measures the amount of memory an algorithm uses relative to the input size. "
        "It includes both auxiliary space (extra space used) and input space."
    )

    pdf.key_concept("Big O Notation (Formal Definition)",
        "Big O notation describes the UPPER BOUND of an algorithm's growth rate.\n"
        "f(n) = O(g(n)) if there exist positive constants c and n0 such that\n"
        "f(n) <= c * g(n) for all n >= n0.\n\n"
        "This means: For large enough inputs, g(n) is always an upper bound on f(n) (up to a constant factor)."
    )

    pdf.chapter_title("How to Calculate Time Complexity", level=2)
    pdf.section_text(
        "Rules for analyzing time complexity:\n"
        "1. Ignore constants: O(2n) becomes O(n)\n"
        "2. Take the dominant term: O(n^2 + n) becomes O(n^2)\n"
        "3. Loops: A single loop over n elements = O(n)\n"
        "4. Nested loops: Two nested loops = O(n^2)\n"
        "5. Sequential statements: Add complexities\n"
        "6. If-else: Take the maximum of both branches"
    )

    pdf.code_block(
        "// O(n) - Single loop\n"
        "for (int i = 0; i < n; i++)\n"
        "    count++;\n\n"
        "// O(n^2) - Nested loop\n"
        "for (int i = 0; i < n; i++)\n"
        "    for (int j = 0; j < n; j++)\n"
        "        count++;\n\n"
        "// O(log n) - Divide by 2 each time\n"
        "while (n > 1)\n"
        "    n = n / 2;\n\n"
        "// O(sqrt(n))\n"
        "for (int i = 1; i * i <= n; i++)\n"
        "    count++;"
    )

    # ========== CHAPTER 3: ARRAYS ==========
    pdf.add_page()
    pdf.chapter_title("3. Arrays")

    pdf.section_text(
        "An array is a collection of elements stored at contiguous memory locations. It is the simplest "
        "and most widely used data structure. Elements can be accessed directly using their index."
    )

    pdf.chapter_title("Array Representation", level=2)
    pdf.visual_box(
        "Index:    0     1     2     3     4\n"
        "        +-----+-----+-----+-----+-----+\n"
        "Value:  | 10  | 20  | 30  | 40  | 50  |\n"
        "        +-----+-----+-----+-----+-----+\n"
        "Memory: 1000  1004  1008  1012  1016\n"
        "(Each int takes 4 bytes)"
    )

    pdf.chapter_title("Key Properties", level=2)
    pdf.section_text(
        "1. Fixed Size: Size must be known at declaration (in most languages)\n"
        "2. Contiguous Memory: Elements are stored side by side\n"
        "3. Direct Access: Access any element in O(1) using index\n"
        "4. Homogeneous: All elements must be of the same type\n"
        "5. Index starts at 0 in most languages (0-based indexing)"
    )

    pdf.chapter_title("Time Complexity of Array Operations", level=2)
    headers = ["Operation", "Time Complexity", "Description"]
    widths = [45, 35, 110]
    pdf.table_header(headers, widths)
    rows = [
        ["Access (by index)", "O(1)", "Direct access using memory address"],
        ["Search (unsorted)", "O(n)", "Linear search through array"],
        ["Search (sorted)", "O(log n)", "Binary search"],
        ["Insert (at end)", "O(1)", "Amortized for dynamic arrays"],
        ["Insert (at start)", "O(n)", "Shift all elements right"],
        ["Insert (at index)", "O(n)", "Shift elements and insert"],
        ["Delete (at end)", "O(1)", "Remove last element"],
        ["Delete (at start)", "O(n)", "Shift all elements left"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Example: Find Maximum Element", level=2)
    pdf.code_block(
        "int findMax(int arr[], int n) {\n"
        "    int maxVal = arr[0];          // O(1)\n"
        "    for (int i = 1; i < n; i++)  // O(n)\n"
        "        if (arr[i] > maxVal)\n"
        "            maxVal = arr[i];     // O(1)\n"
        "    return maxVal;               // Total: O(n)\n"
        "}"
    )

    pdf.chapter_title("Example: Reverse an Array", level=2)
    pdf.code_block(
        "void reverse(int arr[], int n) {\n"
        "    int left = 0, right = n - 1;\n"
        "    while (left < right) {\n"
        "        int temp = arr[left];\n"
        "        arr[left] = arr[right];\n"
        "        arr[right] = temp;\n"
        "        left++;\n"
        "        right--;\n"
        "    }\n"
        "    // Time: O(n), Space: O(1)\n"
        "}"
    )
    pdf.visual_box(
        "Before: [1, 2, 3, 4, 5]\n"
        "Step 1: [5, 2, 3, 4, 1]  swap(0,4)\n"
        "Step 2: [5, 4, 3, 2, 1]  swap(1,3)\n"
        "Left meets Right -> Done!"
    )

    pdf.chapter_title("Two Pointer Technique (Array)", level=2)
    pdf.section_text(
        "The two pointer technique uses two indices to traverse an array, often from opposite ends. "
        "It reduces O(n^2) brute force solutions to O(n)."
    )
    pdf.code_block(
        "// Check if array is a palindrome\n"
        "bool isPalindrome(int arr[], int n) {\n"
        "    int left = 0, right = n - 1;\n"
        "    while (left < right) {\n"
        "        if (arr[left] != arr[right])\n"
        "            return false;\n"
        "        left++;\n"
        "        right--;\n"
        "    }\n"
        "    return true;\n"
        "}"
    )

    pdf.chapter_title("Sliding Window Technique", level=2)
    pdf.section_text(
        "Sliding window is used for problems involving contiguous subarrays of fixed size k. "
        "Instead of recalculating from scratch each time, we slide the window."
    )
    pdf.code_block(
        "// Maximum sum of k consecutive elements\n"
        "int maxSum(int arr[], int n, int k) {\n"
        "    int windowSum = 0;\n"
        "    // Calculate sum of first window\n"
        "    for (int i = 0; i < k; i++)\n"
        "        windowSum += arr[i];\n\n"
        "    int maxSum = windowSum;\n"
        "    // Slide the window\n"
        "    for (int i = k; i < n; i++) {\n"
        "        windowSum += arr[i] - arr[i - k];\n"
        "        maxSum = max(maxSum, windowSum);\n"
        "    }\n"
        "    return maxSum;\n"
        "    // Time: O(n), Space: O(1)\n"
        "}"
    )

    # ========== CHAPTER 4: STRINGS ==========
    pdf.add_page()
    pdf.chapter_title("4. Strings")

    pdf.section_text(
        "A string is a sequence of characters. In most languages, strings are immutable (Java, Python), "
        "meaning each modification creates a new string. Understanding string manipulation is crucial "
        "for interviews."
    )

    pdf.chapter_title("String as an Array", level=2)
    pdf.visual_box(
        "String: \"HELLO\"\n"
        "Index:    0  1  2  3  4\n"
        "Char:    'H''E''L''L''O'\n"
        "ASCII:    72 69 76 76 79"
    )

    pdf.chapter_title("Common String Operations & Their Complexity", level=2)
    headers = ["Operation", "Time", "Notes"]
    widths = [60, 25, 105]
    pdf.table_header(headers, widths)
    rows = [
        ["Access by index", "O(1)", "Same as array"],
        ["Search substring", "O(n*m)", "n = text, m = pattern"],
        ["Concatenation", "O(n+m)", "Creates new string"],
        ["Check palindrome", "O(n)", "Two pointer approach"],
        ["Check anagram", "O(n)", "Character frequency count"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Example: Reverse a String", level=2)
    pdf.code_block(
        "// Python\n"
        "def reverse_string(s):\n"
        "    return s[::-1]  # O(n) time, O(n) space\n\n"
        "// Two-pointer approach (in-place for char array)\n"
        "def reverse_string(s):\n"
        "    left, right = 0, len(s) - 1\n"
        "    while left < right:\n"
        "        s[left], s[right] = s[right], s[left]\n"
        "        left += 1\n"
        "        right -= 1"
    )

    pdf.chapter_title("Example: Check if Two Strings are Anagrams", level=2)
    pdf.section_text(
        "Two strings are anagrams if they contain the same characters with the same frequencies."
    )
    pdf.code_block(
        "def is_anagram(s1, s2):\n"
        "    if len(s1) != len(s2):\n"
        "        return False\n"
        "    # Method 1: Sorting - O(n log n)\n"
        "    return sorted(s1) == sorted(s2)\n\n"
        "def is_anagram(s1, s2):\n"
        "    # Method 2: Frequency count - O(n)\n"
        "    freq = [0] * 26\n"
        "    for c in s1:\n"
        "        freq[ord(c) - ord('a')] += 1\n"
        "    for c in s2:\n"
        "        freq[ord(c) - ord('a')] -= 1\n"
        "    return all(f == 0 for f in freq)"
    )

    pdf.chapter_title("KMP Pattern Matching (Advanced)", level=2)
    pdf.section_text(
        "The Knuth-Morris-Pratt (KMP) algorithm finds a pattern in a text in O(n+m) time, "
        "much better than the naive O(n*m). It uses a 'lps' (longest proper prefix which is also suffix) array."
    )
    pdf.code_block(
        "def kmp_search(text, pattern):\n"
        "    # Step 1: Build LPS array\n"
        "    lps = [0] * len(pattern)\n"
        "    length, i = 0, 1\n"
        "    while i < len(pattern):\n"
        "        if pattern[i] == pattern[length]:\n"
        "            length += 1\n"
        "            lps[i] = length\n"
        "            i += 1\n"
        "        elif length != 0:\n"
        "            length = lps[length - 1]\n"
        "        else:\n"
        "            lps[i] = 0\n"
        "            i += 1\n"
        "    # Step 2: Search\n"
        "    i = j = 0\n"
        "    while i < len(text):\n"
        "        if text[i] == pattern[j]:\n"
        "            i += 1; j += 1\n"
        "        if j == len(pattern):\n"
        "            print(f'Pattern found at {i - j}')\n"
        "            j = lps[j - 1]\n"
        "        elif i < len(text) and text[i] != pattern[j]:\n"
        "            if j != 0: j = lps[j - 1]\n"
        "            else: i += 1"
    )

    # ========== CHAPTER 5: LINKED LISTS ==========
    pdf.add_page()
    pdf.chapter_title("5. Linked Lists")

    pdf.section_text(
        "A linked list is a linear data structure where elements (nodes) are stored in non-contiguous "
        "memory. Each node contains data and a pointer/reference to the next node."
    )

    pdf.chapter_title("Types of Linked Lists", level=2)
    pdf.visual_box(
        "SINGLY LINKED LIST:\n"
        "[1|*]-->[2|*]-->[3|*]-->[4|/]\n\n"
        "DOUBLY LINKED LIST:\n"
        "[/|1|*]<==>[*|2|*]<==>[*|3|*]<==>[*|4|/]\n\n"
        "CIRCULAR LINKED LIST:\n"
        "[1|*]-->[2|*]-->[3|*]-->[4|*]\n"
        "  ^                         |\n"
        "  +-------------------------+\n\n"
        "* = next pointer, / = NULL"
    )

    pdf.chapter_title("Node Structure", level=2)
    pdf.code_block(
        "class Node:\n"
        "    def __init__(self, data):\n"
        "        self.data = data\n"
        "        self.next = None  # pointer to next node\n\n"
        "class DLLNode:\n"
        "    def __init__(self, data):\n"
        "        self.data = data\n"
        "        self.prev = None  # pointer to previous\n"
        "        self.next = None  # pointer to next"
    )

    pdf.chapter_title("Time Complexity", level=2)
    headers = ["Operation", "Singly LL", "Doubly LL", "Description"]
    widths = [45, 30, 30, 85]
    pdf.table_header(headers, widths)
    rows = [
        ["Access by index", "O(n)", "O(n)", "Must traverse from head"],
        ["Search", "O(n)", "O(n)", "Must traverse"],
        ["Insert at head", "O(1)", "O(1)", "Update head pointer"],
        ["Insert at tail", "O(1)*", "O(1)*", "*with tail pointer"],
        ["Insert after node", "O(1)", "O(1)", "Just update pointers"],
        ["Delete at head", "O(1)", "O(1)", "Update head pointer"],
        ["Delete at tail", "O(n)", "O(1)", "Singly: must find prev"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Example: Insert at Beginning", level=2)
    pdf.code_block(
        "def insert_at_head(head, data):\n"
        "    new_node = Node(data)\n"
        "    new_node.next = head  # Point new node to old head\n"
        "    return new_node      # New node becomes head\n"
        "    # Time: O(1), Space: O(1)"
    )
    pdf.visual_box(
        "Insert 5 at head of [1]->[2]->[3]->NULL\n\n"
        "Step 1: Create [5]\n"
        "Step 2: [5]->[1]->[2]->[3]->NULL\n"
        "Step 3: head = [5]"
    )

    pdf.chapter_title("Example: Delete a Node by Value", level=2)
    pdf.code_block(
        "def delete_node(head, key):\n"
        "    # If head needs to be deleted\n"
        "    if head and head.data == key:\n"
        "        return head.next\n"
        "    current = head\n"
        "    while current and current.next:\n"
        "        if current.next.data == key:\n"
        "            current.next = current.next.next\n"
        "            return head\n"
        "        current = current.next\n"
        "    return head\n"
        "    # Time: O(n), Space: O(1)"
    )

    pdf.chapter_title("Detect Cycle (Floyd's Algorithm)", level=2)
    pdf.section_text(
        "Floyd's Cycle Detection uses two pointers (slow and fast). If they meet, there's a cycle. "
        "This is also called the 'Tortoise and Hare' algorithm."
    )
    pdf.code_block(
        "def has_cycle(head):\n"
        "    slow = fast = head\n"
        "    while fast and fast.next:\n"
        "        slow = slow.next       # moves 1 step\n"
        "        fast = fast.next.next  # moves 2 steps\n"
        "        if slow == fast:\n"
        "            return True  # cycle detected!\n"
        "    return False\n"
        "    # Time: O(n), Space: O(1)"
    )
    pdf.visual_box(
        "No cycle:  [1]->[2]->[3]->[4]->NULL\n"
        "Fast reaches NULL -> No cycle\n\n"
        "Cycle:     [1]->[2]->[3]->[4]\n"
        "                  ^         |\n"
        "                  +----<----+\n"
        "Fast and Slow meet at 3 -> Cycle!"
    )

    # ========== CHAPTER 6: STACKS ==========
    pdf.add_page()
    pdf.chapter_title("6. Stacks")

    pdf.section_text(
        "A stack is a Last-In-First-Out (LIFO) data structure. The last element added is the first one "
        "removed. Think of it as a stack of plates - you add and remove from the top only."
    )

    pdf.chapter_title("Stack Operations", level=2)
    pdf.visual_box(
        "    |  40  | <-- TOP (push/pop here)\n"
        "    |  30  |\n"
        "    |  20  |\n"
        "    |  10  |\n"
        "    +------+\n\n"
        "push(50) -> |  50  | <-- TOP\n"
        "            |  40  |\n"
        "            |  30  |\n"
        "            |  20  |\n"
        "            |  10  |"
    )

    pdf.chapter_title("Time Complexity", level=2)
    headers = ["Operation", "Time", "Description"]
    widths = [50, 25, 115]
    pdf.table_header(headers, widths)
    rows = [
        ["push(x)", "O(1)", "Add element to top"],
        ["pop()", "O(1)", "Remove element from top"],
        ["top()/peek()", "O(1)", "View top element without removing"],
        ["isEmpty()", "O(1)", "Check if stack is empty"],
        ["size()", "O(1)", "Get number of elements"],
        ["Search(x)", "O(n)", "Search for element in stack"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Implementation", level=2)
    pdf.code_block(
        "class Stack:\n"
        "    def __init__(self):\n"
        "        self.items = []\n\n"
        "    def push(self, item):\n"
        "        self.items.append(item)\n\n"
        "    def pop(self):\n"
        "        if self.is_empty():\n"
        "            raise IndexError('Stack is empty')\n"
        "        return self.items.pop()\n\n"
        "    def peek(self):\n"
        "        return self.items[-1] if self.items else None\n\n"
        "    def is_empty(self):\n"
        "        return len(self.items) == 0\n\n"
        "    def size(self):\n"
        "        return len(self.items)"
    )

    pdf.chapter_title("Applications of Stack", level=2)
    pdf.section_text(
        "1. Undo/Redo operations in text editors\n"
        "2. Browser back/forward navigation\n"
        "3. Function call stack (recursion)\n"
        "4. Expression evaluation (infix to postfix)\n"
        "5. Balanced parentheses validation\n"
        "6. Tower of Hanoi\n"
        "7. DFS graph traversal"
    )

    pdf.chapter_title("Example: Balanced Parentheses", level=2)
    pdf.code_block(
        "def is_balanced(s):\n"
        "    stack = []\n"
        "    mapping = {')': '(', '}': '{', ']': '['}\n"
        "    for char in s:\n"
        "        if char in mapping.values():  # opening\n"
        "            stack.append(char)\n"
        "        elif char in mapping:  # closing\n"
        "            if not stack or stack[-1] != mapping[char]:\n"
        "                return False\n"
        "            stack.pop()\n"
        "    return len(stack) == 0\n\n"
        "print(is_balanced('({[]})'))  # True\n"
        "print(is_balanced('({[)]}'))  # False"
    )

    pdf.chapter_title("Example: Next Greater Element", level=2)
    pdf.code_block(
        "def next_greater(arr):\n"
        "    n = len(arr)\n"
        "    result = [-1] * n\n"
        "    stack = []  # stores indices\n"
        "    for i in range(n):\n"
        "        while stack and arr[i] > arr[stack[-1]]:\n"
        "            result[stack.pop()] = arr[i]\n"
        "        stack.append(i)\n"
        "    return result\n\n"
        "# Input:  [4, 5, 2, 25]\n"
        "# Output: [5, 25, 25, -1]\n"
        "# Time: O(n), Space: O(n)"
    )

    # ========== CHAPTER 7: QUEUES ==========
    pdf.add_page()
    pdf.chapter_title("7. Queues")

    pdf.section_text(
        "A queue is a First-In-First-Out (FIFO) data structure. Elements are added at the rear (enqueue) "
        "and removed from the front (dequeue). Think of it as a line at a ticket counter."
    )

    pdf.chapter_title("Queue Operations", level=2)
    pdf.visual_box(
        "FRONT                          REAR\n"
        "  |                            |\n"
        "  v                            v\n"
        "[10]  [20]  [30]  [40]  [50]\n\n"
        "enqueue(60):\n"
        "  [10]  [20]  [30]  [40]  [50]  [60]\n\n"
        "dequeue(): removes 10\n"
        "  [20]  [30]  [40]  [50]  [60]"
    )

    pdf.chapter_title("Types of Queues", level=2)
    pdf.section_text(
        "1. Simple Queue: Basic FIFO queue\n"
        "2. Circular Queue: Connects end to beginning, efficient use of space\n"
        "3. Deque (Double-ended Queue): Insert/remove from both ends\n"
        "4. Priority Queue: Elements have priorities, highest priority removed first"
    )

    pdf.chapter_title("Time Complexity", level=2)
    headers = ["Operation", "Simple Queue", "Circular Queue", "Deque"]
    widths = [45, 45, 50, 50]
    pdf.table_header(headers, widths)
    rows = [
        ["Enqueue/Insert", "O(1)*", "O(1)", "O(1)"],
        ["Dequeue/Remove", "O(1)*", "O(1)", "O(1)"],
        ["Front/Peek", "O(1)", "O(1)", "O(1)"],
        ["Search", "O(n)", "O(n)", "O(n)"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Implementation Using Two Stacks", level=2)
    pdf.code_block(
        "class QueueUsingStacks:\n"
        "    def __init__(self):\n"
        "        self.stack_in = []   # for enqueue\n"
        "        self.stack_out = []  # for dequeue\n\n"
        "    def enqueue(self, x):\n"
        "        self.stack_in.append(x)\n\n"
        "    def dequeue(self):\n"
        "        if not self.stack_out:\n"
        "            while self.stack_in:\n"
        "                self.stack_out.append(self.stack_in.pop())\n"
        "        if not self.stack_out:\n"
        "            raise IndexError('Queue is empty')\n"
        "        return self.stack_out.pop()"
    )

    pdf.chapter_title("Applications of Queue", level=2)
    pdf.section_text(
        "1. BFS graph/tree traversal\n"
        "2. CPU scheduling (Round Robin)\n"
        "3. Print queue (jobs in order)\n"
        "4. Buffering (IO buffers, streaming)\n"
        "5. Sliding window problems\n"
        "6. Level-order traversal of trees"
    )

    # ========== CHAPTER 8: HASH TABLES ==========
    pdf.add_page()
    pdf.chapter_title("8. Hash Tables (Hashing)")

    pdf.section_text(
        "A hash table maps keys to values using a hash function. It provides near O(1) average time "
        "for insertions, deletions, and lookups, making it one of the most important data structures."
    )

    pdf.chapter_title("How Hashing Works", level=2)
    pdf.visual_box(
        "Key: \"apple\" -> hash(\"apple\") -> 7\n"
        "Key: \"banana\" -> hash(\"banana\") -> 2\n\n"
        "Hash Table (array of buckets):\n"
        "Index:  0   1   2       3   4   5   6   7\n"
        "      [---|---|\"banana\"|---|---|---|---|\"apple\"]"
    )

    pdf.chapter_title("Collision Handling", level=2)
    pdf.chapter_title("1. Chaining (Open Hashing)", level=3)
    pdf.visual_box(
        "Index 0: -> [\"cat\", 5] -> [\"hat\", 8] -> NULL\n"
        "Index 1: -> NULL\n"
        "Index 2: -> [\"banana\", 3] -> NULL\n"
        "Index 3: -> [\"dog\", 7] -> [\"log\", 2] -> NULL\n"
        "(Each bucket is a linked list)"
    )

    pdf.chapter_title("2. Open Addressing (Closed Hashing)", level=3)
    pdf.section_text(
        "Linear Probing: If index is taken, try (index+1), (index+2), etc.\n"
        "Quadratic Probing: Try (index+1^2), (index+2^2), etc.\n"
        "Double Hashing: Use a second hash function for step size."
    )
    pdf.visual_box(
        "Linear Probing Example:\n"
        "hash(\"apple\") = 3 -> Table[3] = \"apple\"\n"
        "hash(\"grape\") = 3 -> Collision!\n"
        "  -> Table[4] = \"grape\" (try next slot)"
    )

    pdf.chapter_title("Load Factor", level=2)
    pdf.section_text(
        "Load Factor (alpha) = n / k  where n = number of elements, k = number of buckets\n\n"
        "When alpha exceeds a threshold (typically 0.75), the table is resized (rehashed).\n"
        "New table is typically double the size, and all elements are re-inserted.\n"
        "This maintains O(1) average time by keeping collisions rare."
    )

    pdf.chapter_title("Time Complexity", level=2)
    headers = ["Operation", "Average", "Worst Case"]
    widths = [60, 60, 70]
    pdf.table_header(headers, widths)
    rows = [
        ["Insert", "O(1)", "O(n) - all hash to same bucket"],
        ["Search", "O(1)", "O(n)"],
        ["Delete", "O(1)", "O(n)"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Example: Two Sum Problem", level=2)
    pdf.code_block(
        "def two_sum(nums, target):\n"
        "    seen = {}  # hash map\n"
        "    for i, num in enumerate(nums):\n"
        "        complement = target - num\n"
        "        if complement in seen:\n"
        "            return [seen[complement], i]\n"
        "        seen[num] = i\n"
        "    return []\n\n"
        "# nums = [2, 7, 11, 15], target = 9\n"
        "# Output: [0, 1]  (because 2 + 7 = 9)\n"
        "# Time: O(n), Space: O(n)"
    )

    pdf.chapter_title("Frequency Counting Pattern", level=2)
    pdf.code_block(
        "from collections import Counter\n\n"
        "def top_k_frequent(nums, k):\n"
        "    count = Counter(nums)  # O(n)\n"
        "    return [x for x, _ in count.most_common(k)]\n\n"
        "# Or using a hash map manually:\n"
        "def top_k_frequent(nums, k):\n"
        "    freq = {}\n"
        "    for num in nums:\n"
        "        freq[num] = freq.get(num, 0) + 1\n"
        "    return sorted(freq, key=freq.get, reverse=True)[:k]"
    )

    # ========== CHAPTER 9: TREES ==========
    pdf.add_page()
    pdf.chapter_title("9. Trees")

    pdf.section_text(
        "A tree is a hierarchical data structure consisting of nodes connected by edges. "
        "It has a root node at the top, and each node has zero or more children."
    )

    pdf.chapter_title("Tree Terminology", level=2)
    pdf.visual_box(
        "         100            <- Root\n"
        "        /    \\\n"
        "      50      150       <- Children of 100\n"
        "     /  \\      / \\\n"
        "   25    75  125  200   <- Leaves (no children)\n\n"
        "Root: 100 (top node)\n"
        "Parent of 50: 100\n"
        "Children of 50: 25, 75\n"
        "Leaf nodes: 25, 75, 125, 200\n"
        "Height: 2 (edges from root to deepest leaf)\n"
        "Depth/Level: root=0, 50=1, 25=2"
    )

    pdf.chapter_title("Types of Trees", level=2)
    pdf.visual_box(
        "BINARY TREE: Each node has at most 2 children\n"
        "       1\n"
        "      / \\\n"
        "     2   3\n"
        "    / \\\n"
        "   4   5\n\n"
        "FULL BINARY TREE: Every node has 0 or 2 children\n"
        "       1\n"
        "      / \\\n"
        "     2   3\n"
        "    / \\\n"
        "   4   5\n\n"
        "COMPLETE BINARY TREE: All levels full except last\n"
        "(filled left to right)\n"
        "       1\n"
        "      / \\\n"
        "     2   3\n"
        "    / \\  /\n"
        "   4  5 6"
    )

    pdf.chapter_title("Tree Traversals", level=2)
    pdf.section_text(
        "There are two main categories of tree traversal:\n"
        "1. Depth-First Search (DFS): Goes deep before going wide\n"
        "2. Breadth-First Search (BFS): Goes wide before going deep (Level Order)"
    )

    pdf.chapter_title("DFS Traversals (3 types)", level=3)
    pdf.visual_box(
        "Tree for all traversals:\n"
        "         1\n"
        "        / \\\n"
        "       2   3\n"
        "      / \\\n"
        "     4   5\n\n"
        "Inorder (Left, Root, Right):   4 2 5 1 3\n"
        "Preorder (Root, Left, Right):  1 2 4 5 3\n"
        "Postorder (Left, Right, Root): 4 5 2 3 1"
    )

    pdf.code_block(
        "# Binary Tree Node\n"
        "class TreeNode:\n"
        "    def __init__(self, val=0):\n"
        "        self.val = val\n"
        "        self.left = None\n"
        "        self.right = None\n\n"
        "# Inorder: Left -> Root -> Right\n"
        "def inorder(root):\n"
        "    if root:\n"
        "        inorder(root.left)\n"
        "        print(root.val)\n"
        "        inorder(root.right)\n\n"
        "# Preorder: Root -> Left -> Right\n"
        "def preorder(root):\n"
        "    if root:\n"
        "        print(root.val)\n"
        "        preorder(root.left)\n"
        "        preorder(root.right)\n\n"
        "# Postorder: Left -> Right -> Root\n"
        "def postorder(root):\n"
        "    if root:\n"
        "        postorder(root.left)\n"
        "        postorder(root.right)\n"
        "        print(root.val)\n\n"
        "# Level Order (BFS)\n"
        "from collections import deque\n"
        "def level_order(root):\n"
        "    if not root: return []\n"
        "    result, queue = [], deque([root])\n"
        "    while queue:\n"
        "        level = []\n"
        "        for _ in range(len(queue)):\n"
        "            node = queue.popleft()\n"
        "            level.append(node.val)\n"
        "            if node.left:  queue.append(node.left)\n"
        "            if node.right: queue.append(node.right)\n"
        "        result.append(level)\n"
        "    return result"
    )

    pdf.chapter_title("Height and Size of Tree", level=2)
    pdf.code_block(
        "# Height of tree (number of edges on longest path)\n"
        "def height(root):\n"
        "    if root is None:\n"
        "        return -1\n"
        "    return 1 + max(height(root.left), height(root.right))\n\n"
        "# Number of nodes in tree\n"
        "def size(root):\n"
        "    if root is None:\n"
        "        return 0\n"
        "    return 1 + size(root.left) + size(root.right)\n\n"
        "# Check if two trees are identical\n"
        "def is_same(p, q):\n"
        "    if not p and not q: return True\n"
        "    if not p or not q: return False\n"
        "    return (p.val == q.val and\n"
        "            is_same(p.left, q.left) and\n"
        "            is_same(p.right, q.right))"
    )

    # ========== CHAPTER 10: BST ==========
    pdf.add_page()
    pdf.chapter_title("10. Binary Search Trees (BST)")

    pdf.section_text(
        "A Binary Search Tree is a binary tree with a special property: for every node, all values in "
        "the left subtree are smaller, and all values in the right subtree are larger. This enables "
        "efficient searching."
    )

    pdf.chapter_title("BST Property", level=2)
    pdf.visual_box(
        "         50\n"
        "        /  \\\n"
        "      30    70\n"
        "     /  \\  /  \\\n"
        "   20  40 60  80\n\n"
        "Rule: left < root < right (for every node)\n"
        "Inorder traversal gives sorted order: 20 30 40 50 60 70 80"
    )

    pdf.chapter_title("BST Operations", level=2)
    headers = ["Operation", "Average", "Worst (skewed)"]
    widths = [60, 60, 70]
    pdf.table_header(headers, widths)
    rows = [
        ["Search", "O(log n)", "O(n)"],
        ["Insert", "O(log n)", "O(n)"],
        ["Delete", "O(log n)", "O(n)"],
        ["Find Min/Max", "O(log n)", "O(n)"],
        ["Inorder Successor", "O(log n)", "O(n)"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("BST Implementation", level=2)
    pdf.code_block(
        "class BST:\n"
        "    def __init__(self):\n"
        "        self.root = None\n\n"
        "    def insert(self, val):\n"
        "        self.root = self._insert(self.root, val)\n\n"
        "    def _insert(self, node, val):\n"
        "        if not node:\n"
        "            return TreeNode(val)\n"
        "        if val < node.val:\n"
        "            node.left = self._insert(node.left, val)\n"
        "        elif val > node.val:\n"
        "            node.right = self._insert(node.right, val)\n"
        "        return node\n\n"
        "    def search(self, val):\n"
        "        return self._search(self.root, val)\n\n"
        "    def _search(self, node, val):\n"
        "        if not node or node.val == val:\n"
        "            return node\n"
        "        if val < node.val:\n"
        "            return self._search(node.left, val)\n"
        "        return self._search(node.right, val)\n\n"
        "    def delete(self, val):\n"
        "        self.root = self._delete(self.root, val)\n\n"
        "    def _delete(self, node, val):\n"
        "        if not node:\n"
        "            return node\n"
        "        if val < node.val:\n"
        "            node.left = self._delete(node.left, val)\n"
        "        elif val > node.val:\n"
        "            node.right = self._delete(node.right, val)\n"
        "        else:  # found the node\n"
        "            # Case 1 & 2: no child or one child\n"
        "            if not node.left:\n"
        "                return node.right\n"
        "            if not node.right:\n"
        "                return node.left\n"
        "            # Case 3: two children\n"
        "            # Replace with inorder successor (min of right subtree)\n"
        "            successor = self._min_node(node.right)\n"
        "            node.val = successor.val\n"
        "            node.right = self._delete(node.right, successor.val)\n"
        "        return node"
    )

    pdf.chapter_title("Visual: BST Deletion Cases", level=2)
    pdf.visual_box(
        "Case 1: Delete leaf (40) - just remove\n"
        "    50          50\n"
        "   /  \\        /  \\\n"
        "  30   70  -> 30   70\n"
        " /  \\        /\n"
        "20  [40]    20\n\n"
        "Case 2: Delete node with one child (70)\n"
        "    50          50\n"
        "   /  \\        /  \\\n"
        "  30   [70] -> 30   80\n"
        " /            /\n"
        "20          20\n\n"
        "Case 3: Delete node with two children (50)\n"
        "    [50]         60\n"
        "   /  \\        /  \\\n"
        "  30   70  -> 30   70\n"
        " /  \\  /\\   /  \\  /\\\n"
        "20 40 60 80 20 40 60 80\n"
        "(Replace with inorder successor: 60)"
    )

    # ========== CHAPTER 11: HEAPS ==========
    pdf.add_page()
    pdf.chapter_title("11. Heaps & Priority Queues")

    pdf.section_text(
        "A heap is a complete binary tree that satisfies the heap property. "
        "In a Max-Heap, every parent is >= its children. In a Min-Heap, every parent is <= its children."
    )

    pdf.chapter_title("Max-Heap vs Min-Heap", level=2)
    pdf.visual_box(
        "MAX-HEAP:                  MIN-HEAP:\n"
        "       100                       10\n"
        "      /    \\                   /    \\\n"
        "    80      90               20      30\n"
        "   /  \\    /  \\             /  \\    /  \\\n"
        "  50  60  70  40           40  50  60  70\n\n"
        "Max-Heap: parent >= children\n"
        "Min-Heap: parent <= children"
    )

    pdf.chapter_title("Array Representation of Heap", level=2)
    pdf.section_text(
        "Heaps are typically stored as arrays. For a node at index i:\n"
        "- Parent: (i-1)/2\n"
        "- Left child: 2*i + 1\n"
        "- Right child: 2*i + 2"
    )
    pdf.visual_box(
        "Max-Heap:       100\n"
        "               /    \\\n"
        "             80      90\n"
        "            /  \\    /  \\\n"
        "           50  60  70  40\n\n"
        "Array: [100, 80, 90, 50, 60, 70, 40]\n"
        "Index:   0   1   2   3   4   5   6\n\n"
        "parent(5) = (5-1)/2 = 2 -> value 90\n"
        "left(2)  = 2*2+1 = 5 -> value 70\n"
        "right(2) = 2*2+2 = 6 -> value 40"
    )

    pdf.chapter_title("Heap Operations", level=2)
    headers = ["Operation", "Time", "Description"]
    widths = [50, 25, 115]
    pdf.table_header(headers, widths)
    rows = [
        ["Get Min/Max", "O(1)", "Root element"],
        ["Insert", "O(log n)", "Add at end, bubble up"],
        ["Extract Min/Max", "O(log n)", "Remove root, heapify"],
        ["Build Heap", "O(n)", "From unsorted array"],
        ["Heap Sort", "O(n log n)", "Repeated extraction"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Example: Top K Elements", level=2)
    pdf.section_text(
        "Heaps are perfect for finding the K largest/smallest elements efficiently."
    )
    pdf.code_block(
        "import heapq\n\n"
        "# Find K largest elements - O(n log k)\n"
        "def top_k_largest(nums, k):\n"
        "    return heapq.nlargest(k, nums)\n\n"
        "# Find K smallest elements - O(n log k)\n"
        "def top_k_smallest(nums, k):\n"
        "    return heapq.nsmallest(k, nums)\n\n"
        "# Find Kth largest element\n"
        "def kth_largest(nums, k):\n"
        "    min_heap = []\n"
        "    for num in nums:\n"
        "        heapq.heappush(min_heap, num)\n"
        "        if len(min_heap) > k:\n"
        "            heapq.heappop(min_heap)\n"
        "    return min_heap[0]\n"
        "    # Time: O(n log k), Space: O(k)"
    )

    pdf.chapter_title("Priority Queue Applications", level=2)
    pdf.section_text(
        "1. Dijkstra's shortest path algorithm\n"
        "2. Task scheduling (OS processes)\n"
        "3. Merge K sorted lists/arrays\n"
        "4. Median of a data stream\n"
        "5. Find Kth largest element\n"
        "6. Huffman encoding (compression)"
    )

    # ========== CHAPTER 12: GRAPHS ==========
    pdf.add_page()
    pdf.chapter_title("12. Graphs")

    pdf.section_text(
        "A graph is a collection of vertices (nodes) and edges (connections between nodes). "
        "Graphs are used to model relationships between objects - social networks, maps, networks, etc."
    )

    pdf.chapter_title("Graph Types", level=2)
    pdf.visual_box(
        "UNDIRECTED:              DIRECTED (Digraph):\n"
        "  A --- B                  A --> B\n"
        "  |   / |                  |     |\n"
        "  |  /  |                  v     v\n"
        "  C --- D                  C --> D\n\n"
        "WEIGHTED:                UNWEIGHTED:\n"
        "  A --5-- B                A --- B\n"
        "  |      /|                |   / |\n"
        "  3    4  2                |  /  |\n"
        "  |  /    |                C --- D\n"
        "  C --6-- D"
    )

    pdf.chapter_title("Graph Representations", level=2)
    pdf.chapter_title("1. Adjacency Matrix", level=3)
    pdf.visual_box(
        "Graph: A-B, A-C, B-C, B-D, C-D\n\n"
        "  Matrix:  A  B  C  D\n"
        "  A:      [0, 1, 1, 0]\n"
        "  B:      [1, 0, 1, 1]\n"
        "  C:      [1, 1, 0, 1]\n"
        "  D:      [0, 1, 1, 0]\n\n"
        "Space: O(V^2), Check edge: O(1)"
    )

    pdf.chapter_title("2. Adjacency List", level=3)
    pdf.visual_box(
        "A -> [B, C]\n"
        "B -> [A, C, D]\n"
        "C -> [A, B, D]\n"
        "D -> [B, C]\n\n"
        "Space: O(V+E), Check edge: O(degree)"
    )

    pdf.chapter_title("Comparison", level=3)
    headers = ["Feature", "Adj Matrix", "Adj List"]
    widths = [50, 70, 70]
    pdf.table_header(headers, widths)
    rows = [
        ["Space", "O(V^2)", "O(V+E)"],
        ["Check Edge", "O(1)", "O(degree)"],
        ["List Neighbors", "O(V)", "O(degree)"],
        ["Add Edge", "O(1)", "O(1)"],
        ["Best For", "Dense graphs", "Sparse graphs"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Graph Implementation", level=2)
    pdf.code_block(
        "# Adjacency List using Dictionary\n"
        "class Graph:\n"
        "    def __init__(self):\n"
        "        self.adj = {}\n\n"
        "    def add_vertex(self, v):\n"
        "        if v not in self.adj:\n"
        "            self.adj[v] = []\n\n"
        "    def add_edge(self, u, v, directed=False):\n"
        "        self.add_vertex(u)\n"
        "        self.add_vertex(v)\n"
        "        self.adj[u].append(v)\n"
        "        if not directed:\n"
        "            self.adj[v].append(u)\n\n"
        "    def bfs(self, start):\n"
        "        visited = set()\n"
        "        queue = deque([start])\n"
        "        visited.add(start)\n"
        "        order = []\n"
        "        while queue:\n"
        "            node = queue.popleft()\n"
        "            order.append(node)\n"
        "            for neighbor in self.adj[node]:\n"
        "                if neighbor not in visited:\n"
        "                    visited.add(neighbor)\n"
        "                    queue.append(neighbor)\n"
        "        return order\n\n"
        "    def dfs(self, start, visited=None):\n"
        "        if visited is None:\n"
        "            visited = set()\n"
        "        visited.add(start)\n"
        "        order = [start]\n"
        "        for neighbor in self.adj[start]:\n"
        "            if neighbor not in visited:\n"
        "                order.extend(self.dfs(neighbor, visited))\n"
        "        return order"
    )

    # ========== CHAPTER 13: GRAPH ALGORITHMS ==========
    pdf.add_page()
    pdf.chapter_title("13. Graph Algorithms")

    pdf.chapter_title("BFS vs DFS", level=2)
    pdf.visual_box(
        "BFS (Breadth-First Search):        DFS (Depth-First Search):\n"
        "Explores all neighbors first,       Goes deep along each branch\n"
        "then moves to next level.\n"
        "Uses a QUEUE.                       Uses a STACK or recursion.\n\n"
        "       1                               1\n"
        "      / \\                             / \\\n"
        "     2   3                           2   3\n"
        "    / \\                             / \\\n"
        "   4   5                           4   5\n\n"
        "BFS order: 1,2,3,4,5                DFS order: 1,2,4,5,3\n"
        "Level by level                       Deep first, then backtrack"
    )

    pdf.chapter_title("Dijkstra's Shortest Path Algorithm", level=2)
    pdf.section_text(
        "Finds the shortest path from a source vertex to all other vertices in a weighted graph "
        "with non-negative edge weights. Uses a min-heap (priority queue)."
    )
    pdf.code_block(
        "import heapq\n\n"
        "def dijkstra(graph, source):\n"
        "    dist = {v: float('inf') for v in graph}\n"
        "    dist[source] = 0\n"
        "    pq = [(0, source)]  # (distance, vertex)\n\n"
        "    while pq:\n"
        "        d, u = heapq.heappop(pq)\n"
        "        if d > dist[u]:\n"
        "            continue  # stale entry\n"
        "        for v, weight in graph[u]:\n"
        "            if dist[u] + weight < dist[v]:\n"
        "                dist[v] = dist[u] + weight\n"
        "                heapq.heappush(pq, (dist[v], v))\n"
        "    return dist\n"
        "    # Time: O((V+E) log V) with min-heap"
    )

    pdf.chapter_title("Bellman-Ford Algorithm", level=2)
    pdf.section_text(
        "Handles negative edge weights (unlike Dijkstra). Detects negative cycles.\n"
        "Relaxes all edges V-1 times. If any distance can still be reduced, negative cycle exists."
    )
    pdf.code_block(
        "def bellman_ford(V, edges, source):\n"
        "    dist = [float('inf')] * V\n"
        "    dist[source] = 0\n\n"
        "    # Relax all edges V-1 times\n"
        "    for _ in range(V - 1):\n"
        "        for u, v, w in edges:\n"
        "            if dist[u] + w < dist[v]:\n"
        "                dist[v] = dist[u] + w\n\n"
        "    # Check for negative cycles\n"
        "    for u, v, w in edges:\n"
        "        if dist[u] + w < dist[v]:\n"
        "            print('Negative cycle detected!')\n"
        "            return None\n"
        "    return dist\n"
        "    # Time: O(V * E)"
    )

    pdf.chapter_title("Topological Sorting", level=2)
    pdf.section_text(
        "Linear ordering of vertices in a Directed Acyclic Graph (DAG) such that for every edge "
        "u->v, u comes before v. Used in task scheduling, build systems, course prerequisites."
    )
    pdf.code_block(
        "# Kahn's Algorithm (BFS-based)\n"
        "from collections import deque\n"
        "def topological_sort(V, adj):\n"
        "    in_degree = [0] * V\n"
        "    for u in range(V):\n"
        "        for v in adj[u]:\n"
        "            in_degree[v] += 1\n\n"
        "    queue = deque([i for i in range(V) if in_degree[i] == 0])\n"
        "    result = []\n\n"
        "    while queue:\n"
        "        u = queue.popleft()\n"
        "        result.append(u)\n"
        "        for v in adj[u]:\n"
        "            in_degree[v] -= 1\n"
        "            if in_degree[v] == 0:\n"
        "                queue.append(v)\n\n"
        "    if len(result) != V:\n"
        "        return None  # cycle exists\n"
        "    return result"
    )

    pdf.chapter_title("Minimum Spanning Tree", level=2)
    pdf.section_text(
        "An MST connects all vertices with minimum total edge weight, with no cycles.\n"
        "Kruskal's Algorithm: Sort edges, add if no cycle (uses Union-Find)\n"
        "Prim's Algorithm: Grow MST from a starting vertex (uses priority queue)"
    )

    # ========== CHAPTER 14: SORTING ==========
    pdf.add_page()
    pdf.chapter_title("14. Sorting Algorithms")

    pdf.chapter_title("Comparison of Sorting Algorithms", level=2)
    headers = ["Algorithm", "Best", "Average", "Worst", "Space"]
    widths = [35, 30, 30, 30, 35]
    pdf.table_header(headers, widths)
    rows = [
        ["Bubble Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)"],
        ["Selection Sort", "O(n^2)", "O(n^2)", "O(n^2)", "O(1)"],
        ["Insertion Sort", "O(n)", "O(n^2)", "O(n^2)", "O(1)"],
        ["Merge Sort", "O(nlg)", "O(nlg)", "O(nlg)", "O(n)"],
        ["Quick Sort", "O(nlg)", "O(nlg)", "O(n^2)", "O(lgn)"],
        ["Heap Sort", "O(nlg)", "O(nlg)", "O(nlg)", "O(1)"],
        ["Counting Sort", "O(n+k)", "O(n+k)", "O(n+k)", "O(k)"],
        ["Radix Sort", "O(nk)", "O(nk)", "O(nk)", "O(n+k)"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Bubble Sort", level=2)
    pdf.section_text(
        "Repeatedly swaps adjacent elements if they are in wrong order. "
        "The largest element 'bubbles up' to the end in each pass."
    )
    pdf.visual_box(
        "Pass 1: [5,3,8,1,2] -> [3,5,1,2,8]  (8 bubbled to end)\n"
        "Pass 2: [3,5,1,2,8] -> [3,1,2,5,8]  (5 bubbled)\n"
        "Pass 3: [3,1,2,5,8] -> [1,2,3,5,8]  (3 bubbled)\n"
        "Pass 4: [1,2,3,5,8] -> [1,2,3,5,8]  (no swaps = done!)"
    )
    pdf.code_block(
        "def bubble_sort(arr):\n"
        "    n = len(arr)\n"
        "    for i in range(n):\n"
        "        swapped = False\n"
        "        for j in range(0, n - i - 1):\n"
        "            if arr[j] > arr[j + 1]:\n"
        "                arr[j], arr[j+1] = arr[j+1], arr[j]\n"
        "                swapped = True\n"
        "        if not swapped:  # optimization\n"
        "            break  # already sorted"
    )

    pdf.chapter_title("Merge Sort (Divide & Conquer)", level=2)
    pdf.section_text(
        "Divide array into halves, recursively sort each half, then merge. "
        "Guaranteed O(n log n) but uses O(n) extra space."
    )
    pdf.visual_box(
        "        [38, 27, 43, 3, 9, 82, 10]\n"
        "        /                        \\\n"
        "  [38, 27, 43, 3]        [9, 82, 10]\n"
        "   /          \\            /       \\\n"
        " [38, 27]  [43, 3]    [9, 82]   [10]\n"
        "  /   \\    /   \\      /   \\       |\n"
        "[38] [27] [43] [3]  [9]  [82]    [10]\n"
        "  \\   /    \\   /      \\   /       |\n"
        " [27,38]  [3,43]    [9,82]      [10]\n"
        "   \\          \\            \\       /\n"
        "  [3,27,38,43]          [9,10,82]\n"
        "        \\                        /\n"
        "     [3, 9, 10, 27, 38, 43, 82]"
    )
    pdf.code_block(
        "def merge_sort(arr):\n"
        "    if len(arr) <= 1:\n"
        "        return arr\n"
        "    mid = len(arr) // 2\n"
        "    left = merge_sort(arr[:mid])\n"
        "    right = merge_sort(arr[mid:])\n"
        "    return merge(left, right)\n\n"
        "def merge(left, right):\n"
        "    result = []\n"
        "    i = j = 0\n"
        "    while i < len(left) and j < len(right):\n"
        "        if left[i] <= right[j]:\n"
        "            result.append(left[i])\n"
        "            i += 1\n"
        "        else:\n"
        "            result.append(right[j])\n"
        "            j += 1\n"
        "    result.extend(left[i:])\n"
        "    result.extend(right[j:])\n"
        "    return result"
    )

    pdf.add_page()
    pdf.chapter_title("Quick Sort", level=2)
    pdf.section_text(
        "Picks a pivot, partitions array so elements smaller than pivot are on the left, "
        "larger on the right, then recursively sorts both halves. Best and average case O(n log n)."
    )
    pdf.code_block(
        "def quick_sort(arr, low, high):\n"
        "    if low < high:\n"
        "        pivot_idx = partition(arr, low, high)\n"
        "        quick_sort(arr, low, pivot_idx - 1)\n"
        "        quick_sort(arr, pivot_idx + 1, high)\n\n"
        "def partition(arr, low, high):\n"
        "    pivot = arr[high]  # last element as pivot\n"
        "    i = low - 1  # index of smaller element\n"
        "    for j in range(low, high):\n"
        "        if arr[j] < pivot:\n"
        "            i += 1\n"
        "            arr[i], arr[j] = arr[j], arr[i]\n"
        "    arr[i+1], arr[high] = arr[high], arr[i+1]\n"
        "    return i + 1"
    )
    pdf.visual_box(
        "Array: [10, 80, 30, 90, 40, 50, 70]\n"
        "Pivot = 70\n"
        "After partition: [10, 30, 40, 50, 70, 90, 80]\n"
        "                  smaller   ^   larger\n"
        "                         pivot\n"
        "Then recursively sort [10,30,40,50] and [90,80]"
    )

    pdf.chapter_title("Insertion Sort", level=2)
    pdf.section_text(
        "Builds sorted array one element at a time. Picks each element and inserts it into its "
        "correct position in the already-sorted portion. Efficient for small or nearly sorted data."
    )
    pdf.code_block(
        "def insertion_sort(arr):\n"
        "    for i in range(1, len(arr)):\n"
        "        key = arr[i]\n"
        "        j = i - 1\n"
        "        while j >= 0 and arr[j] > key:\n"
        "            arr[j + 1] = arr[j]  # shift right\n"
        "            j -= 1\n"
        "        arr[j + 1] = key\n"
        "    # Best: O(n) when already sorted\n"
        "    # Worst: O(n^2) when reverse sorted"
    )

    # ========== CHAPTER 15: SEARCHING ==========
    pdf.add_page()
    pdf.chapter_title("15. Searching Algorithms")

    pdf.chapter_title("Linear Search", level=2)
    pdf.section_text(
        "Simple search through each element. Works on both sorted and unsorted arrays. O(n) time."
    )
    pdf.code_block(
        "def linear_search(arr, target):\n"
        "    for i in range(len(arr)):\n"
        "        if arr[i] == target:\n"
        "            return i\n"
        "    return -1"
    )

    pdf.chapter_title("Binary Search", level=2)
    pdf.section_text(
        "Efficient search on sorted arrays. Repeatedly divides search space in half.\n"
        "Time: O(log n) - extremely efficient. Eliminates half the remaining elements each step."
    )
    pdf.visual_box(
        "Sorted array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]\n"
        "Target: 23\n\n"
        "Step 1: mid = arr[4] = 16 < 23 -> search right\n"
        "Step 2: mid = arr[7] = 56 > 23 -> search left\n"
        "Step 3: mid = arr[5] = 23 = 23 -> FOUND at index 5!\n\n"
        "10 elements searched in just 3 steps (log2(10) ~ 3.3)"
    )
    pdf.code_block(
        "# Iterative Binary Search\n"
        "def binary_search(arr, target):\n"
        "    low, high = 0, len(arr) - 1\n"
        "    while low <= high:\n"
        "        mid = (low + high) // 2\n"
        "        if arr[mid] == target:\n"
        "            return mid\n"
        "        elif arr[mid] < target:\n"
        "            low = mid + 1\n"
        "        else:\n"
        "            high = mid - 1\n"
        "    return -1\n\n"
        "# Recursive Binary Search\n"
        "def binary_search_rec(arr, target, low, high):\n"
        "    if low > high:\n"
        "        return -1\n"
        "    mid = (low + high) // 2\n"
        "    if arr[mid] == target:\n"
        "        return mid\n"
        "    elif arr[mid] < target:\n"
        "        return binary_search_rec(arr, target, mid+1, high)\n"
        "    else:\n"
        "        return binary_search_rec(arr, target, low, mid-1)"
    )

    pdf.chapter_title("Binary Search Variants", level=2)
    pdf.section_text(
        "1. First Occurrence: Find the first position of target in a sorted array with duplicates\n"
        "2. Last Occurrence: Find the last position of target\n"
        "3. Search in Rotated Sorted Array: Array rotated at some pivot\n"
        "4. Find Floor/Ceiling: Closest value <= or >= target\n"
        "5. Square Root: Find integer square root using binary search"
    )
    pdf.code_block(
        "# First occurrence of target\n"
        "def first_occurrence(arr, target):\n"
        "    low, high = 0, len(arr) - 1\n"
        "    result = -1\n"
        "    while low <= high:\n"
        "        mid = (low + high) // 2\n"
        "        if arr[mid] == target:\n"
        "            result = mid\n"
        "            high = mid - 1  # keep searching left\n"
        "        elif arr[mid] < target:\n"
        "            low = mid + 1\n"
        "        else:\n"
        "            high = mid - 1\n"
        "    return result\n\n"
        "# Search in rotated sorted array\n"
        "def search_rotated(arr, target):\n"
        "    low, high = 0, len(arr) - 1\n"
        "    while low <= high:\n"
        "        mid = (low + high) // 2\n"
        "        if arr[mid] == target:\n"
        "            return mid\n"
        "        # Left half is sorted\n"
        "        if arr[low] <= arr[mid]:\n"
        "            if arr[low] <= target < arr[mid]:\n"
        "                high = mid - 1\n"
        "            else:\n"
        "                low = mid + 1\n"
        "        else:  # Right half is sorted\n"
        "            if arr[mid] < target <= arr[high]:\n"
        "                low = mid + 1\n"
        "            else:\n"
        "                high = mid - 1\n"
        "    return -1"
    )

    # ========== CHAPTER 16: DYNAMIC PROGRAMMING ==========
    pdf.add_page()
    pdf.chapter_title("16. Dynamic Programming (DP)")

    pdf.section_text(
        "Dynamic Programming is an algorithmic technique for solving problems by breaking them into "
        "overlapping subproblems and storing the results to avoid redundant computation. "
        "It applies when a problem has:\n"
        "1. Optimal Substructure: Optimal solution contains optimal solutions to subproblems\n"
        "2. Overlapping Subproblems: Same subproblems are solved repeatedly"
    )

    pdf.chapter_title("DP Approaches", level=2)
    pdf.section_text(
        "1. Top-Down (Memoization): Start from main problem, recurse down, cache results\n"
        "2. Bottom-Up (Tabulation): Start from smallest subproblems, build up to answer"
    )

    pdf.chapter_title("Example 1: Fibonacci Numbers", level=2)
    pdf.code_block(
        "# Brute Force - O(2^n) - EXPONENTIAL\n"
        "def fib(n):\n"
        "    if n <= 1: return n\n"
        "    return fib(n-1) + fib(n-2)  # repeated work!\n\n"
        "# Top-Down (Memoization) - O(n)\n"
        "def fib_memo(n, memo={}):\n"
        "    if n in memo: return memo[n]\n"
        "    if n <= 1: return n\n"
        "    memo[n] = fib_memo(n-1) + fib_memo(n-2)\n"
        "    return memo[n]\n\n"
        "# Bottom-Up (Tabulation) - O(n)\n"
        "def fib_tab(n):\n"
        "    if n <= 1: return n\n"
        "    dp = [0] * (n + 1)\n"
        "    dp[1] = 1\n"
        "    for i in range(2, n + 1):\n"
        "        dp[i] = dp[i-1] + dp[i-2]\n"
        "    return dp[n]\n\n"
        "# Space Optimized - O(n) time, O(1) space\n"
        "def fib_opt(n):\n"
        "    if n <= 1: return n\n"
        "    a, b = 0, 1\n"
        "    for _ in range(2, n + 1):\n"
        "        a, b = b, a + b\n"
        "    return b"
    )
    pdf.visual_box(
        "Fib(5) Recursion Tree (without memoization):\n"
        "              fib(5)\n"
        "            /       \\\n"
        "        fib(4)     fib(3)     <-- fib(3) computed TWICE!\n"
        "       /     \\     /    \\\n"
        "    fib(3) fib(2) fib(2) fib(1)\n"
        "   /   \\\n"
        "fib(2) fib(1)\n\n"
        "With memoization, each fib(k) computed only once: O(n)"
    )

    pdf.chapter_title("Example 2: 0/1 Knapsack Problem", level=2)
    pdf.section_text(
        "Given items with weights and values, and a knapsack with capacity W, find the maximum value "
        "you can carry. Each item can be taken at most once."
    )
    pdf.code_block(
        "def knapsack(weights, values, W):\n"
        "    n = len(weights)\n"
        "    # dp[i][w] = max value using first i items with capacity w\n"
        "    dp = [[0] * (W + 1) for _ in range(n + 1)]\n\n"
        "    for i in range(1, n + 1):\n"
        "        for w in range(W + 1):\n"
        "            # Don't take item i\n"
        "            dp[i][w] = dp[i-1][w]\n"
        "            # Take item i (if it fits)\n"
        "            if weights[i-1] <= w:\n"
        "                dp[i][w] = max(dp[i][w],\n"
        "                    dp[i-1][w - weights[i-1]] + values[i-1])\n"
        "    return dp[n][W]\n\n"
        "# Example:\n"
        "# weights = [1, 3, 4, 5]\n"
        "# values  = [1, 4, 5, 7]\n"
        "# W = 7\n"
        "# Answer: 9 (items with weight 3 and 4)"
    )

    pdf.chapter_title("Example 3: Longest Common Subsequence", level=2)
    pdf.code_block(
        "def lcs(s1, s2):\n"
        "    m, n = len(s1), len(s2)\n"
        "    dp = [[0] * (n + 1) for _ in range(m + 1)]\n\n"
        "    for i in range(1, m + 1):\n"
        "        for j in range(1, n + 1):\n"
        "            if s1[i-1] == s2[j-1]:\n"
        "                dp[i][j] = dp[i-1][j-1] + 1\n"
        "            else:\n"
        "                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n"
        "    return dp[m][n]\n\n"
        "# LCS of \"ABCBDAB\" and \"BDCAB\" = 4 (BCAB)"
    )

    pdf.chapter_title("Common DP Patterns", level=2)
    pdf.section_text(
        "1. Fibonacci Pattern: dp[i] = dp[i-1] + dp[i-2]\n"
        "2. Knapsack Pattern: dp[i][w] = max(include, exclude)\n"
        "3. LCS Pattern: Match or skip characters\n"
        "4. Matrix Chain: dp[i][j] = min over all splits\n"
        "5. LIS Pattern: dp[i] = max length ending at i\n"
        "6. Coin Change: dp[amount] = min coins to make amount\n"
        "7. Grid Paths: dp[i][j] = ways to reach (i,j)"
    )

    pdf.chapter_title("Example 4: Coin Change", level=2)
    pdf.code_block(
        "def coin_change(coins, amount):\n"
        "    dp = [float('inf')] * (amount + 1)\n"
        "    dp[0] = 0  # 0 coins needed for amount 0\n\n"
        "    for i in range(1, amount + 1):\n"
        "        for coin in coins:\n"
        "            if coin <= i and dp[i - coin] + 1 < dp[i]:\n"
        "                dp[i] = dp[i - coin] + 1\n"
        "    return dp[amount] if dp[amount] != float('inf') else -1\n\n"
        "# coins = [1, 5, 10, 25], amount = 30\n"
        "# Answer: 2 (25 + 5)"
    )

    # ========== CHAPTER 17: GREEDY ==========
    pdf.add_page()
    pdf.chapter_title("17. Greedy Algorithms")

    pdf.section_text(
        "Greedy algorithms make the locally optimal choice at each step, hoping to find the global "
        "optimum. They work when the problem has:\n"
        "1. Greedy Choice Property: A global optimum can be arrived at by selecting a local optimum\n"
        "2. Optimal Substructure: An optimal solution to the problem contains optimal solutions to subproblems"
    )

    pdf.chapter_title("Greedy vs Dynamic Programming", level=2)
    headers = ["Feature", "Greedy", "Dynamic Programming"]
    widths = [50, 70, 70]
    pdf.table_header(headers, widths)
    rows = [
        ["Approach", "Local optimum", "All subproblems"],
        ["Choice", "One path", "Consider all options"],
        ["Guarantee", "Not always optimal", "Always optimal"],
        ["Time", "Usually faster", "Usually slower"],
        ["Example", "Activity Selection", "Knapsack"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Example: Activity Selection Problem", level=2)
    pdf.code_block(
        "# Select maximum non-overlapping activities\n"
        "def activity_selection(activities):\n"
        "    # activities = [(start, end), ...]\n"
        "    activities.sort(key=lambda x: x[1])  # sort by end time\n"
        "    selected = [activities[0]]\n"
        "    last_end = activities[0][1]\n\n"
        "    for i in range(1, len(activities)):\n"
        "        if activities[i][0] >= last_end:  # no overlap\n"
        "            selected.append(activities[i])\n"
        "            last_end = activities[i][1]\n"
        "    return selected\n\n"
        "# Activities: [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11)]\n"
        "# Selected:   [(1,4),(5,7),(8,11)]"
    )

    pdf.chapter_title("Example: Fractional Knapsack", level=2)
    pdf.code_block(
        "def fractional_knapsack(weights, values, W):\n"
        "    n = len(weights)\n"
        "    # Calculate value-to-weight ratio\n"
        "    items = [(values[i]/weights[i], weights[i], values[i])\n"
        "             for i in range(n)]\n"
        "    items.sort(reverse=True)  # sort by ratio\n\n"
        "    total = 0\n"
        "    for ratio, w, v in items:\n"
        "        if w <= W:\n"
        "            total += v\n"
        "            W -= w\n"
        "        else:\n"
        "            total += v * (W / w)  # take fraction\n"
        "            break\n"
        "    return total"
    )

    pdf.chapter_title("Other Greedy Problems", level=2)
    pdf.section_text(
        "1. Job Sequencing: Sort by deadline, select profitable jobs\n"
        "2. Huffman Coding: Build optimal prefix codes (compression)\n"
        "3. Minimum Platforms: Sort arrivals and departures\n"
        "4. Jump Game: Track the farthest reachable position\n"
        "5. Gas Station: Find starting point for circular tour"
    )

    # ========== CHAPTER 18: BACKTRACKING ==========
    pdf.add_page()
    pdf.chapter_title("18. Backtracking")

    pdf.section_text(
        "Backtracking is a systematic method for exploring all possible solutions. It builds a solution "
        "incrementally and backtracks when it determines the current path cannot lead to a valid solution. "
        "It's essentially a depth-first search on a state-space tree."
    )

    pdf.chapter_title("Backtracking Template", level=2)
    pdf.code_block(
        "def backtrack(path, choices):\n"
        "    if end_condition_met:\n"
        "        result.append(path[:])  # record solution\n"
        "        return\n"
        "    for choice in choices:\n"
        "        if not valid:\n"
        "            continue  # prune\n"
        "        path.append(choice)     # choose\n"
        "        backtrack(path, new_choices)  # explore\n"
        "        path.pop()              # un-choose (backtrack)"
    )

    pdf.chapter_title("Example 1: N-Queens Problem", level=2)
    pdf.section_text(
        "Place N queens on an N×N chessboard such that no two queens attack each other "
        "(no two in same row, column, or diagonal)."
    )
    pdf.visual_box(
        "4-Queens Solution:\n"
        "    . Q . .\n"
        "    . . . Q\n"
        "    Q . . .\n"
        "    . . Q .\n\n"
        "Each queen is in a unique row, column, and diagonal."
    )
    pdf.code_block(
        "def solve_n_queens(n):\n"
        "    board = [['.'] * n for _ in range(n)]\n"
        "    result = []\n\n"
        "    def is_safe(row, col):\n"
        "        for i in range(row):\n"
        "            if board[i][col] == 'Q': return False\n"
        "            if col - (row-i) >= 0 and board[i][col-(row-i)] == 'Q':\n"
        "                return False\n"
        "            if col + (row-i) < n and board[i][col+(row-i)] == 'Q':\n"
        "                return False\n"
        "        return True\n\n"
        "    def backtrack(row):\n"
        "        if row == n:\n"
        "            result.append([''.join(r) for r in board])\n"
        "            return\n"
        "        for col in range(n):\n"
        "            if is_safe(row, col):\n"
        "                board[row][col] = 'Q'\n"
        "                backtrack(row + 1)\n"
        "                board[row][col] = '.'  # backtrack\n\n"
        "    backtrack(0)\n"
        "    return result"
    )

    pdf.chapter_title("Example 2: Subset Sum Problem", level=2)
    pdf.code_block(
        "def subset_sum(nums, target):\n"
        "    result = []\n"
        "    def backtrack(start, path, remaining):\n"
        "        if remaining == 0:\n"
        "            result.append(path[:])\n"
        "            return\n"
        "        if remaining < 0:\n"
        "            return\n"
        "        for i in range(start, len(nums)):\n"
        "            path.append(nums[i])\n"
        "            backtrack(i + 1, path, remaining - nums[i])\n"
        "            path.pop()  # backtrack\n"
        "    backtrack(0, [], target)\n"
        "    return result\n\n"
        "# nums = [2,3,6,7], target = 7\n"
        "# Output: [[2, 5], [7]]  (if 5 were in list)"
    )

    pdf.chapter_title("Example 3: Generate Permutations", level=2)
    pdf.code_block(
        "def permute(nums):\n"
        "    result = []\n"
        "    def backtrack(path, remaining):\n"
        "        if not remaining:\n"
        "            result.append(path[:])\n"
        "            return\n"
        "        for i in range(len(remaining)):\n"
        "            path.append(remaining[i])\n"
        "            backtrack(path, remaining[:i] + remaining[i+1:])\n"
        "            path.pop()\n"
        "    backtrack([], nums)\n"
        "    return result\n\n"
        "# nums = [1,2,3]\n"
        "# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"
    )

    # ========== CHAPTER 19: TRIE ==========
    pdf.add_page()
    pdf.chapter_title("19. Trie (Prefix Tree)")

    pdf.section_text(
        "A Trie is a tree-like data structure used for efficient retrieval of keys in a dataset of strings. "
        "Each node represents a character, and paths from root to marked nodes represent stored strings."
    )

    pdf.chapter_title("Trie Structure", level=2)
    pdf.visual_box(
        "Insert: \"cat\", \"car\", \"card\", \"dog\", \"dot\"\n\n"
        "         root\n"
        "        /   \\\n"
        "       c     d\n"
        "      /       \\\n"
        "     a         o\n"
        "    / \\       / \\\n"
        "   t*  r*    g*  t*\n"
        "       |\n"
        "       d*\n\n"
        "* = end of word marker\n"
        "From root -> c -> a -> t = \"cat\"\n"
        "From root -> c -> a -> r -> d = \"card\""
    )

    pdf.chapter_title("Trie Implementation", level=2)
    pdf.code_block(
        "class TrieNode:\n"
        "    def __init__(self):\n"
        "        self.children = {}\n"
        "        self.is_end = False\n\n"
        "class Trie:\n"
        "    def __init__(self):\n"
        "        self.root = TrieNode()\n\n"
        "    def insert(self, word):\n"
        "        node = self.root\n"
        "        for char in word:\n"
        "            if char not in node.children:\n"
        "                node.children[char] = TrieNode()\n"
        "            node = node.children[char]\n"
        "        node.is_end = True\n\n"
        "    def search(self, word):\n"
        "        node = self.root\n"
        "        for char in word:\n"
        "            if char not in node.children:\n"
        "                return False\n"
        "            node = node.children[char]\n"
        "        return node.is_end\n\n"
        "    def starts_with(self, prefix):\n"
        "        node = self.root\n"
        "        for char in prefix:\n"
        "            if char not in node.children:\n"
        "                return False\n"
        "            node = node.children[char]\n"
        "        return True"
    )

    pdf.chapter_title("Time Complexity", level=2)
    headers = ["Operation", "Time"]
    widths = [80, 110]
    pdf.table_header(headers, widths)
    rows = [
        ["Insert", "O(m) where m = word length"],
        ["Search", "O(m)"],
        ["Starts With", "O(m)"],
        ["Delete", "O(m)"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    pdf.ln(5)
    pdf.chapter_title("Applications", level=2)
    pdf.section_text(
        "1. Autocomplete / Search suggestions\n"
        "2. Spell checking\n"
        "3. IP routing (longest prefix match)\n"
        "4. Word games (Boggle, Scrabble)\n"
        "5. Predictive text input"
    )

    # ========== CHAPTER 20: UNION-FIND ==========
    pdf.add_page()
    pdf.chapter_title("20. Union-Find (Disjoint Set Union)")

    pdf.section_text(
        "Union-Find is a data structure that tracks a set of elements partitioned into disjoint "
        "(non-overlapping) subsets. It supports two operations:\n"
        "1. Find: Determine which set an element belongs to\n"
        "2. Union: Merge two sets into one"
    )

    pdf.chapter_title("How It Works", level=2)
    pdf.visual_box(
        "Initial: Each element is its own set\n"
        "{0} {1} {2} {3} {4} {5}\n\n"
        "Union(0,1): {0,1} {2} {3} {4} {5}\n"
        "Union(2,3): {0,1} {2,3} {4} {5}\n"
        "Union(0,2): {0,1,2,3} {4} {5}\n"
        "Union(4,5): {0,1,2,3} {4,5}\n"
        "Union(0,4): {0,1,2,3,4,5}  (all connected!)"
    )

    pdf.chapter_title("Optimizations", level=2)
    pdf.section_text(
        "1. Path Compression: During find, make each node point directly to root\n"
        "2. Union by Rank: Attach smaller tree under larger tree root\n"
        "With both optimizations: nearly O(1) per operation (amortized)"
    )

    pdf.code_block(
        "class UnionFind:\n"
        "    def __init__(self, n):\n"
        "        self.parent = list(range(n))\n"
        "        self.rank = [0] * n\n\n"
        "    def find(self, x):\n"
        "        if self.parent[x] != x:\n"
        "            self.parent[x] = self.find(self.parent[x])  # path compression\n"
        "        return self.parent[x]\n\n"
        "    def union(self, x, y):\n"
        "        px, py = self.find(x), self.find(y)\n"
        "        if px == py: return False  # already connected\n"
        "        if self.rank[px] < self.rank[py]:\n"
        "            px, py = py, px\n"
        "        self.parent[py] = px  # attach smaller under larger\n"
        "        if self.rank[px] == self.rank[py]:\n"
        "            self.rank[px] += 1\n"
        "        return True\n\n"
        "    def connected(self, x, y):\n"
        "        return self.find(x) == self.find(y)"
    )

    pdf.chapter_title("Applications", level=2)
    pdf.section_text(
        "1. Kruskal's Minimum Spanning Tree algorithm\n"
        "2. Detecting cycles in undirected graphs\n"
        "3. Finding connected components\n"
        "4. Network connectivity problems\n"
        "5. Image processing (connected pixels)"
    )

    # ========== CHAPTER 21: PRACTICE PROBLEMS ==========
    pdf.add_page()
    pdf.chapter_title("21. Practice Problems Collection")

    pdf.section_text(
        "Here is a curated collection of practice problems organized by topic. "
        "Start with Easy problems and progress to Hard ones. These are common in coding interviews."
    )

    # Arrays
    pdf.chapter_title("Arrays", level=2)
    pdf.practice_problem("A1", "Two Sum", "Easy",
        "Given an array of integers nums and an integer target, return indices of the two numbers that add up to target. "
        "Each input has exactly one solution. Use hash map for O(n) solution.",
        "Think about what complement you need for each number.")
    pdf.practice_problem("A2", "Best Time to Buy and Sell Stock", "Easy",
        "Given prices[i] is the price of a stock on day i. Find the maximum profit from buying and selling once. "
        "You must buy before selling.",
        "Track minimum price seen so far.")
    pdf.practice_problem("A3", "Product of Array Except Self", "Medium",
        "Given an array, return an array where each element is the product of all other elements. "
        "Do not use division. Solve in O(n) without using the output array as extra space.",
        "Use prefix and suffix product arrays.")
    pdf.practice_problem("A4", "Container With Most Water", "Medium",
        "Given n non-negative integers a1,a2,...,an representing container heights, find two lines that "
        "together with the x-axis form a container that holds the most water.",
        "Two pointer from both ends, move the shorter one.")
    pdf.practice_problem("A5", "Trapping Rain Water", "Hard",
        "Given n non-negative integers representing an elevation map, compute how much water it can trap after raining.",
        "For each position, water = min(max_left, max_right) - height[i].")
    pdf.practice_problem("A6", "Maximum Subarray (Kadane's)", "Medium",
        "Find the contiguous subarray with the largest sum and return its sum.",
        "dp[i] = max(arr[i], dp[i-1] + arr[i]). Track global max.")

    # Linked Lists
    pdf.chapter_title("Linked Lists", level=2)
    pdf.practice_problem("L1", "Reverse a Linked List", "Easy",
        "Reverse a singly linked list iteratively and recursively.",
        "Use three pointers: prev, curr, next.")
    pdf.practice_problem("L2", "Merge Two Sorted Lists", "Easy",
        "Merge two sorted linked lists into one sorted list.",
        "Compare heads and attach smaller node.")
    pdf.practice_problem("L3", "Detect Cycle", "Easy",
        "Determine if a linked list has a cycle using O(1) space.",
        "Floyd's tortoise and hare algorithm.")
    pdf.practice_problem("L4", "Remove Nth Node From End", "Medium",
        "Remove the nth node from the end of a linked list in one pass.",
        "Use two pointers with n gap.")
    pdf.practice_problem("L5", "Merge K Sorted Lists", "Hard",
        "Merge k sorted linked lists into one sorted list efficiently.",
        "Use a min-heap of size k.")

    # Stacks & Queues
    pdf.chapter_title("Stacks & Queues", level=2)
    pdf.practice_problem("S1", "Valid Parentheses", "Easy",
        "Given a string containing just '(', ')', '{', '}', '[' and ']', determine if the input is valid.",
        "Push opening brackets, pop and match closing ones.")
    pdf.practice_problem("S2", "Min Stack", "Medium",
        "Design a stack that supports push, pop, top, and retrieving the minimum element in O(1) time.",
        "Use an auxiliary stack to track minimums.")
    pdf.practice_problem("S3", "Daily Temperatures", "Medium",
        "Given daily temperatures, find how many days you have to wait for a warmer temperature.",
        "Use a monotonic stack storing indices.")
    pdf.practice_problem("S4", "Evaluate Reverse Polish Notation", "Medium",
        "Evaluate the value of an arithmetic expression in Reverse Polish Notation (postfix).",
        "Push numbers, pop two for each operator.")

    # Trees
    pdf.chapter_title("Trees", level=2)
    pdf.practice_problem("T1", "Maximum Depth of Binary Tree", "Easy",
        "Find the maximum depth (height) of a binary tree.",
        "return 1 + max(depth(left), depth(right)).")
    pdf.practice_problem("T2", "Validate BST", "Medium",
        "Check if a binary tree is a valid Binary Search Tree.",
        "Pass min/max bounds down during recursion.")
    pdf.practice_problem("T3", "Lowest Common Ancestor", "Medium",
        "Find the lowest common ancestor of two nodes in a binary tree.",
        "If both nodes are in left/right subtree, recurse there. Otherwise, current node is LCA.")
    pdf.practice_problem("T4", "Serialize and Deserialize Binary Tree", "Hard",
        "Design an algorithm to serialize a binary tree to a string and deserialize it back.",
        "Use preorder traversal with null markers.")
    pdf.practice_problem("T5", "Binary Tree Level Order Traversal", "Medium",
        "Return the level order traversal of a binary tree's nodes' values (left to right, level by level).",
        "Use BFS with a queue.")

    # Graphs
    pdf.chapter_title("Graphs", level=2)
    pdf.practice_problem("G1", "Number of Islands", "Medium",
        "Given a 2D grid of '1's (land) and '0's (water), count the number of islands.",
        "BFS/DFS to mark visited cells for each island.")
    pdf.practice_problem("G2", "Clone Graph", "Medium",
        "Deep copy a connected undirected graph.",
        "BFS/DFS with a hashmap to map original to clone.")
    pdf.practice_problem("G3", "Course Schedule (Topological Sort)", "Medium",
        "Determine if you can finish all courses given prerequisites (detect cycle in directed graph).",
        "Kahn's algorithm or DFS with cycle detection.")
    pdf.practice_problem("G4", "Word Ladder", "Hard",
        "Find the shortest transformation sequence from beginWord to endWord, changing one letter at a time.",
        "BFS level by level. Build word set for O(1) lookup.")
    pdf.practice_problem("G5", "Network Delay Time", "Medium",
        "Find the time it takes for all nodes to receive a signal from a source node.",
        "Run Dijkstra's algorithm from source.")

    # Dynamic Programming
    pdf.chapter_title("Dynamic Programming", level=2)
    pdf.practice_problem("D1", "Climbing Stairs", "Easy",
        "You can climb 1 or 2 steps. How many distinct ways to reach the nth step?",
        "It's Fibonacci: ways(n) = ways(n-1) + ways(n-2).")
    pdf.practice_problem("D2", "Longest Increasing Subsequence", "Medium",
        "Find the length of the longest strictly increasing subsequence.",
        "dp[i] = length of LIS ending at i. Or use patience sorting O(n log n).")
    pdf.practice_problem("D3", "Coin Change", "Medium",
        "Find the fewest coins needed to make up an amount. Return -1 if not possible.",
        "dp[amount] = min(dp[amount - coin] + 1 for each coin).")
    pdf.practice_problem("D4", "Longest Palindromic Substring", "Medium",
        "Find the longest palindromic substring (not subsequence).",
        "Expand around center for each position. O(n^2) time, O(1) space.")
    pdf.practice_problem("D5", "Edit Distance", "Medium",
        "Find the minimum number of operations (insert, delete, replace) to convert word1 to word2.",
        "dp[i][j] = min operations to convert word1[:i] to word2[:j].")
    pdf.practice_problem("D6", "House Robber", "Medium",
        "Rob houses in a line for max money. Adjacent houses trigger alarm.",
        "dp[i] = max(dp[i-1], dp[i-2] + nums[i]).")

    pdf.add_page()
    pdf.chapter_title("Quick Reference: Problem Patterns", level=2)
    headers = ["Pattern", "When to Use", "Example Problems"]
    widths = [35, 65, 90]
    pdf.table_header(headers, widths)
    rows = [
        ["Two Pointer", "Sorted array, pairs", "Two Sum, Container Water"],
        ["Sliding Window", "Contiguous subarray", "Max Subarray Sum, Min Window"],
        ["Hash Map", "Frequency, lookup", "Two Sum, Group Anagrams"],
        ["Binary Search", "Sorted, search space", "Rotated Array, Sqrt"],
        ["BFS", "Level order, shortest path", "Word Ladder, Islands"],
        ["DFS", "Exhaustive, path finding", "Permutations, N-Queens"],
        ["DP", "Overlapping subproblems", "Knapsack, LCS, LIS"],
        ["Greedy", "Local optimal", "Activity Selection, Huffman"],
        ["Stack", "Parentheses, next greater", "Valid Parentheses, Min Stack"],
        ["Heap", "Top K, median", "Top K Elements, Merge K Lists"],
        ["Union-Find", "Connected components", "Redundant Connection"],
        ["Trie", "String prefix search", "Autocomplete, Word Search"],
    ]
    for i, row in enumerate(rows):
        pdf.table_row(row, widths, fill=(i % 2 == 0))

    # ========== APPENDIX ==========
    pdf.add_page()
    pdf.chapter_title("Appendix: How to Approach DSA Problems")

    pdf.chapter_title("Step-by-Step Problem Solving", level=2)
    pdf.section_text(
        "1. READ: Understand the problem completely. What are the inputs? What's the expected output?\n"
        "2. EXAMPLES: Work through 2-3 examples by hand, including edge cases.\n"
        "3. BRUTE FORCE: Come up with a naive solution. This helps understand the problem.\n"
        "4. OPTIMIZE: Can you eliminate unnecessary work? Use the right data structure.\n"
        "5. CODE: Write clean, readable code. Use meaningful variable names.\n"
        "6. TEST: Walk through your code with your examples. Check edge cases.\n"
        "7. ANALYZE: State the time and space complexity."
    )

    pdf.chapter_title("Common Interview Tips", level=2)
    pdf.section_text(
        "1. Think out loud - explain your approach before coding.\n"
        "2. Ask clarifying questions about constraints and edge cases.\n"
        "3. Start with the brute force solution, then optimize.\n"
        "4. If stuck, try the brute force first - partial credit is better than nothing.\n"
        "5. Use edge cases: empty input, single element, duplicates, negative numbers.\n"
        "6. Test your code mentally with small examples.\n"
        "7. Be ready to discuss time and space complexity.\n"
        "8. Practice consistently - solve 2-3 problems daily."
    )

    pdf.chapter_title("Recommended Learning Path", level=2)
    pdf.section_text(
        "Week 1-2: Arrays, Strings, Time Complexity\n"
        "Week 3-4: Linked Lists, Stacks, Queues\n"
        "Week 5-6: Trees, BST, Heaps\n"
        "Week 7-8: Hashing, Graphs (BFS, DFS)\n"
        "Week 9-10: Sorting, Searching\n"
        "Week 11-12: Dynamic Programming basics\n"
        "Week 13-14: Advanced DP, Greedy, Backtracking\n"
        "Week 15+: Practice interview problems, mock interviews"
    )

    pdf.chapter_title("Resources for Further Learning", level=2)
    pdf.section_text(
        "- LeetCode: leetcode.com (problem practice)\n"
        "- NeetCode 150: neetcode.io (curated problem list)\n"
        "- Striver's SDE Sheet: takeuforward.org (structured preparation)\n"
        "- CLRS: Introduction to Algorithms (textbook)\n"
        "- Visualgo.net: Visualize algorithms\n"
        "- Big O Cheat Sheet: bigocheatsheet.com"
    )

    # Save
    pdf.output("DSA_Learning_Guide.pdf")
    print("PDF generated successfully: DSA_Learning_Guide.pdf")
    print(f"Total pages: {pdf.page_no()}")


if __name__ == "__main__":
    build_pdf()
