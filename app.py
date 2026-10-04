
import streamlit as st
import streamlit.components.v1 as components
import json
import html

st.set_page_config(
    page_title="Sort Studio",
    layout="wide",
    initial_sidebar_state="collapsed",
)

PENGUIN_URL = "https://assets-v2.lottiefiles.com/a/8b304b9c-b8a8-11ef-b541-cbac9caf0959/Se1jz5vRP6.png"
CAT_URL = "https://assets-v2.lottiefiles.com/a/658d659c-1173-11ee-847f-4b67b46a99bb/7VMoQZeghP.png"

st.markdown("""
<style>
:root{
  --bg:#fff8fc;
  --panel:#ffffff;
  --panel-soft:#fff1f7;
  --ink:#2f2933;
  --muted:#7f7381;
  --line:#efdfe8;
  --accent:#d86496;
  --accent-soft:#f9d9e8;
  --accent-dark:#a64471;
  --code:#241f25;
}
html,body,[class*="css"]{
  font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}
.stApp{
  background:
    radial-gradient(circle at 8% 2%, rgba(255,255,255,.95), transparent 26%),
    linear-gradient(180deg,#fff9fc 0%,#fff6fb 100%);
  color:var(--ink);
}
header[data-testid="stHeader"]{
  background:transparent;
}
.block-container{
  max-width:1120px;
  padding-top:2.5rem !important;
  padding-bottom:4rem;
}
h1{
  font-size:clamp(2.1rem,4vw,3.5rem) !important;
  line-height:1.08 !important;
  letter-spacing:-.04em;
  color:var(--ink) !important;
  margin:0 0 .45rem !important;
}
h2{
  font-size:1.55rem !important;
  letter-spacing:-.025em;
  color:var(--ink) !important;
  margin-top:2.2rem !important;
}
h3{
  color:var(--ink) !important;
}
p,li{
  line-height:1.7;
}
.hero{
  padding:1rem 0 1.2rem;
}
.hero-kicker{
  font-size:.78rem;
  font-weight:800;
  text-transform:uppercase;
  letter-spacing:.16em;
  color:var(--accent-dark);
  margin-bottom:.8rem;
}
.hero-copy{
  color:var(--muted);
  font-size:1.08rem;
  max-width:690px;
}
.home-grid{
  display:grid;
  grid-template-columns:repeat(2,minmax(0,1fr));
  gap:14px;
  margin-top:1.8rem;
}
.home-card{
  border:1px solid var(--line);
  background:rgba(255,255,255,.88);
  border-radius:18px;
  padding:1.05rem 1.1rem;
  min-height:112px;
}
.home-card-title{
  font-weight:800;
  font-size:1.04rem;
  margin-bottom:.35rem;
}
.home-card-copy{
  color:var(--muted);
  font-size:.92rem;
}
.section{
  border-top:1px solid var(--line);
  padding-top:1.5rem;
  margin-top:1.7rem;
}
.clean-card{
  border:1px solid var(--line);
  background:rgba(255,255,255,.84);
  border-radius:18px;
  padding:1.1rem 1.2rem;
}
.note{
  border-left:3px solid var(--accent);
  padding:.75rem 0 .75rem 1rem;
  color:#5f5361;
  margin:.6rem 0;
}
.metric-row{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:10px;
  margin-top:1rem;
}
.metric{
  border:1px solid var(--line);
  border-radius:14px;
  padding:.8rem .9rem;
  background:#fff;
}
.metric-label{
  color:var(--muted);
  font-size:.78rem;
  font-weight:700;
  text-transform:uppercase;
  letter-spacing:.08em;
}
.metric-value{
  font-weight:800;
  margin-top:.25rem;
}
.cat-note{
  display:flex;
  align-items:center;
  gap:14px;
  border:1px solid var(--line);
  background:#fff;
  border-radius:18px;
  padding:.8rem 1rem;
  margin:.8rem 0 1rem;
}
.cat-note img{
  width:72px;
  height:72px;
  object-fit:contain;
  border-radius:14px;
}
.cat-note-text{
  color:#5e535e;
  font-size:.94rem;
}
.stButton>button{
  width:100%;
  border:1px solid var(--line) !important;
  background:#fff !important;
  color:var(--ink) !important;
  font-weight:750 !important;
  border-radius:14px !important;
  min-height:46px;
  box-shadow:none !important;
  transition:border-color .15s ease, background .15s ease, transform .15s ease;
}
.stButton>button:hover{
  border-color:#dca5be !important;
  background:#fff8fb !important;
  transform:translateY(-1px);
}
div[data-testid="stCode"]{
  border:1px solid #ded6dc;
  border-radius:16px;
  overflow:hidden;
}
[data-testid="stTextInput"] input{
  border-radius:12px;
  border:1px solid #dfd3da;
  background:white;
}
[data-testid="stExpander"]{
  background:#fff;
  border:1px solid var(--line) !important;
  border-radius:14px !important;
}
.navline{
  color:var(--muted);
  font-size:.9rem;
  margin-bottom:1rem;
}
.small-credit{
  color:#9b8e9b;
  font-size:.75rem;
  margin-top:2rem;
  border-top:1px solid var(--line);
  padding-top:1rem;
}
@media(max-width:700px){
  .home-grid,.metric-row{grid-template-columns:1fr}
  .block-container{padding-top:1.6rem !important}
}
</style>
""", unsafe_allow_html=True)

ALGORITHMS = [
    "Selection Sort",
    "Bubble Sort",
    "Insertion Sort",
    "Merge Sort",
    "Quick Sort",
    "Recursive Bubble Sort",
    "Recursive Insertion Sort",
    "Arrays",
]

DATA = {
"Selection Sort":{
    "summary":"Find the smallest value in the unsorted part and place it at the current position.",
    "memory":"Select the minimum, swap it forward, then shrink the unsorted part.",
    "time":"O(n²)",
    "space":"O(1)",
    "stable":"No",
},
"Bubble Sort":{
    "summary":"Compare neighboring values and swap them when they are in the wrong order.",
    "memory":"After each full pass, the largest remaining value has bubbled to the right.",
    "time":"O(n²)",
    "space":"O(1)",
    "stable":"Yes",
},
"Insertion Sort":{
    "summary":"Grow a sorted left side by inserting each new value into its correct position.",
    "memory":"Pick a key, shift larger values right, then insert the key into the gap.",
    "time":"O(n²)",
    "space":"O(1)",
    "stable":"Yes",
},
"Merge Sort":{
    "summary":"Split the array into smaller halves, sort them, then merge them back together.",
    "memory":"Divide first. Merge in sorted order second.",
    "time":"O(n log n)",
    "space":"O(n)",
    "stable":"Yes",
},
"Quick Sort":{
    "summary":"Choose a pivot, partition smaller values to one side and larger values to the other, then recurse.",
    "memory":"Pivot, partition, recurse on the left and right sections.",
    "time":"O(n log n) average",
    "space":"O(log n) average",
    "stable":"Usually no",
},
"Recursive Bubble Sort":{
    "summary":"Perform one bubble pass, then recursively sort one fewer element.",
    "memory":"One pass fixes the largest value, then call the same function with n - 1.",
    "time":"O(n²)",
    "space":"O(n) recursion",
    "stable":"Yes",
},
"Recursive Insertion Sort":{
    "summary":"Recursively sort the first n - 1 values, then insert the final value correctly.",
    "memory":"Sort the smaller prefix first, then insert the last key.",
    "time":"O(n²)",
    "space":"O(n) recursion",
    "stable":"Yes",
},
}

JAVA = {
"Selection Sort":"""public static void selectionSort(int[] arr) {
    int n = arr.length;

    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;

        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        int temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }
}""",
"Bubble Sort":"""public static void bubbleSort(int[] arr) {
    int n = arr.length;

    for (int i = 0; i < n - 1; i++) {
        boolean swapped = false;

        for (int j = 0; j < n - 1 - i; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }

        if (!swapped) break;
    }
}""",
"Insertion Sort":"""public static void insertionSort(int[] arr) {
    for (int i = 1; i < arr.length; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}""",
"Merge Sort":"""public static void mergeSort(int[] arr, int left, int right) {
    if (left >= right) return;

    int mid = left + (right - left) / 2;

    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}

private static void merge(int[] arr, int left, int mid, int right) {
    int[] temp = new int[right - left + 1];

    int i = left;
    int j = mid + 1;
    int k = 0;

    while (i <= mid && j <= right) {
        if (arr[i] <= arr[j]) temp[k++] = arr[i++];
        else temp[k++] = arr[j++];
    }

    while (i <= mid) temp[k++] = arr[i++];
    while (j <= right) temp[k++] = arr[j++];

    for (int x = 0; x < temp.length; x++) {
        arr[left + x] = temp[x];
    }
}""",
"Quick Sort":"""public static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pivotIndex = partition(arr, low, high);

        quickSort(arr, low, pivotIndex - 1);
        quickSort(arr, pivotIndex + 1, high);
    }
}

private static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}""",
"Recursive Bubble Sort":"""public static void recursiveBubbleSort(int[] arr, int n) {
    if (n == 1) return;

    for (int i = 0; i < n - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            int temp = arr[i];
            arr[i] = arr[i + 1];
            arr[i + 1] = temp;
        }
    }

    recursiveBubbleSort(arr, n - 1);
}""",
"Recursive Insertion Sort":"""public static void recursiveInsertionSort(int[] arr, int n) {
    if (n <= 1) return;

    recursiveInsertionSort(arr, n - 1);

    int key = arr[n - 1];
    int j = n - 2;

    while (j >= 0 && arr[j] > key) {
        arr[j + 1] = arr[j];
        j--;
    }

    arr[j + 1] = key;
}""",
}

EXPLAIN = {
"Selection Sort":[
("for (int i = 0; i < n - 1; i++)","Choose the next position that needs its correct value."),
("int minIndex = i;","Assume the current value is the smallest for now."),
("for (int j = i + 1; j < n; j++)","Search only the unsorted part to the right."),
("if (arr[j] < arr[minIndex])","If a smaller value is found, remember its index."),
("swap arr[i] and arr[minIndex]","Put the smallest found value into position i."),
],
"Bubble Sort":[
("for (int i = 0; i < n - 1; i++)","Each outer loop is one full bubble pass."),
("for (int j = 0; j < n - 1 - i; j++)","Only scan the unsorted part."),
("if (arr[j] > arr[j + 1])","Check whether neighboring values are in the wrong order."),
("swap the two values","Move the larger neighbor one position to the right."),
("if (!swapped) break;","If nothing moved, the array was already sorted."),
],
"Insertion Sort":[
("int key = arr[i];","Pick the next value that must be inserted."),
("int j = i - 1;","Start comparing from the end of the sorted left side."),
("while (j >= 0 && arr[j] > key)","Keep going left while values are too large."),
("arr[j + 1] = arr[j];","Shift each large value one place right."),
("arr[j + 1] = key;","Insert the key into the gap that remains."),
],
"Merge Sort":[
("if (left >= right) return;","A section with one value is already sorted."),
("int mid = ...","Find the midpoint so the array can be divided."),
("mergeSort(...left...)","Recursively sort the left half."),
("mergeSort(...right...)","Recursively sort the right half."),
("merge(...)","Combine both sorted halves in increasing order."),
],
"Quick Sort":[
("int pivot = arr[high];","Use the last value as the pivot."),
("if (arr[j] <= pivot)","Values smaller than or equal to the pivot belong on the left."),
("swap arr[i] and arr[j]","Expand the smaller-values region."),
("place pivot at i + 1","Move the pivot into its final sorted position."),
("quickSort(...)","Repeat the same process on both sides of the pivot."),
],
"Recursive Bubble Sort":[
("if (n == 1) return;","Base case: one value is already sorted."),
("for (int i = 0; i < n - 1; i++)","Perform one normal bubble pass."),
("recursiveBubbleSort(arr, n - 1);","The largest value is fixed, so recurse on one fewer value."),
],
"Recursive Insertion Sort":[
("if (n <= 1) return;","Base case: one value is already sorted."),
("recursiveInsertionSort(arr, n - 1);","First sort the smaller prefix."),
("int key = arr[n - 1];","Pick the final value as the key."),
("while (j >= 0 && arr[j] > key)","Shift larger values right."),
("arr[j + 1] = key;","Insert the key into its final position."),
],
}

def parse_nums(raw):
    try:
        nums = [int(x.strip()) for x in raw.split(",") if x.strip()]
    except ValueError:
        return None
    if not 2 <= len(nums) <= 8:
        return None
    return nums

def init_items(nums):
    return [{"id":f"p{i}","value":v} for i,v in enumerate(nums)]

def snap(steps, items, active=(), note="", state="normal"):
    steps.append({
        "items":[dict(x) for x in items],
        "active":list(active),
        "note":note,
        "state":state,
    })

def selection_steps(nums):
    a=init_items(nums); s=[]
    snap(s,a,note="Start from the first unsorted position.")
    for i in range(len(a)-1):
        m=i
        snap(s,a,[a[i]["id"]],f"Position {i}: search for the smallest remaining value.","focus")
        for j in range(i+1,len(a)):
            snap(s,a,[a[m]["id"],a[j]["id"]],f"Compare {a[m]['value']} with {a[j]['value']}.","compare")
            if a[j]["value"] < a[m]["value"]:
                m=j
                snap(s,a,[a[m]["id"]],f"{a[m]['value']} is the smallest seen so far.","focus")
        if m != i:
            x,y=a[i]["value"],a[m]["value"]
            active=[a[i]["id"],a[m]["id"]]
            a[i],a[m]=a[m],a[i]
            snap(s,a,active,f"Swap {x} and {y}.","swap")
    snap(s,a,[x["id"] for x in a],"Sorted.","done")
    return s

def bubble_steps(nums):
    a=init_items(nums); s=[]
    snap(s,a,note="Compare neighbors from left to right.")
    n=len(a)
    for i in range(n-1):
        moved=False
        for j in range(n-1-i):
            ids=[a[j]["id"],a[j+1]["id"]]
            snap(s,a,ids,f"Compare {a[j]['value']} and {a[j+1]['value']}.","compare")
            if a[j]["value"] > a[j+1]["value"]:
                left,right=a[j]["value"],a[j+1]["value"]
                a[j],a[j+1]=a[j+1],a[j]
                moved=True
                snap(s,a,ids,f"Swap them. {left} moves right.","swap")
        if not moved:
            break
    snap(s,a,[x["id"] for x in a],"Sorted.","done")
    return s

def insertion_steps(nums):
    a=init_items(nums); s=[]
    snap(s,a,[a[0]["id"]],"The first penguin is already a sorted group of one.")
    for i in range(1,len(a)):
        key=a[i]
        snap(s,a,[key["id"]],f"Pick {key['value']} as the key.","focus")
        j=i-1
        while j>=0 and a[j]["value"] > key["value"]:
            moving=a[j]
            a[j+1]=moving
            snap(s,a,[moving["id"],key["id"]],f"Shift {moving['value']} one place right.","swap")
            j-=1
        a[j+1]=key
        snap(s,a,[key["id"]],f"Insert {key['value']} here.","focus")
    snap(s,a,[x["id"] for x in a],"Sorted.","done")
    return s

def merge_steps(nums):
    a=init_items(nums); s=[]
    snap(s,a,note="Split, sort, and merge.")
    def ms(l,r):
        if l>=r:
            return
        m=(l+r)//2
        snap(s,a,[x["id"] for x in a[l:r+1]],f"Split positions {l} to {r}.","focus")
        ms(l,m); ms(m+1,r)
        left=a[l:m+1]
        right=a[m+1:r+1]
        merged=[]
        i=j=0
        while i<len(left) and j<len(right):
            active=[left[i]["id"],right[j]["id"]]
            snap(s,a,active,f"Compare {left[i]['value']} and {right[j]['value']}.","compare")
            if left[i]["value"] <= right[j]["value"]:
                merged.append(left[i]); i+=1
            else:
                merged.append(right[j]); j+=1
        merged += left[i:] + right[j:]
        a[l:r+1]=merged
        snap(s,a,[x["id"] for x in merged],"Merge the section back in sorted order.","swap")
    ms(0,len(a)-1)
    snap(s,a,[x["id"] for x in a],"Sorted.","done")
    return s

def quick_steps(nums):
    a=init_items(nums); s=[]
    snap(s,a,note="Partition around a pivot.")
    def qs(lo,hi):
        if lo>=hi:
            return
        pivot=a[hi]
        snap(s,a,[pivot["id"]],f"Use {pivot['value']} as the pivot.","focus")
        i=lo-1
        for j in range(lo,hi):
            snap(s,a,[a[j]["id"],pivot["id"]],f"Compare {a[j]['value']} with pivot {pivot['value']}.","compare")
            if a[j]["value"] <= pivot["value"]:
                i+=1
                if i != j:
                    ids=[a[i]["id"],a[j]["id"]]
                    a[i],a[j]=a[j],a[i]
                    snap(s,a,ids,"Move the smaller value to the left partition.","swap")
        p=i+1
        ids=[a[p]["id"],a[hi]["id"]]
        a[p],a[hi]=a[hi],a[p]
        snap(s,a,ids,f"Place pivot {a[p]['value']} in its final position.","swap")
        qs(lo,p-1); qs(p+1,hi)
    qs(0,len(a)-1)
    snap(s,a,[x["id"] for x in a],"Sorted.","done")
    return s

def recursive_bubble_steps(nums):
    a=init_items(nums); s=[]
    snap(s,a,note="One bubble pass, then recurse on n - 1.")
    def rb(n):
        if n<=1:
            return
        for i in range(n-1):
            ids=[a[i]["id"],a[i+1]["id"]]
            snap(s,a,ids,f"Compare {a[i]['value']} and {a[i+1]['value']}.","compare")
            if a[i]["value"] > a[i+1]["value"]:
                a[i],a[i+1]=a[i+1],a[i]
                snap(s,a,ids,"Swap the neighbors.","swap")
        snap(s,a,[a[n-1]["id"]],f"Last position of this pass is fixed. Recurse with n = {n-1}.","focus")
        rb(n-1)
    rb(len(a))
    snap(s,a,[x["id"] for x in a],"Sorted.","done")
    return s

def recursive_insertion_steps(nums):
    a=init_items(nums); s=[]
    snap(s,a,note="Recursively sort the prefix, then insert the last value.")
    def ri(n):
        if n<=1:
            return
        snap(s,a,[x["id"] for x in a[:n-1]],f"First sort the first {n-1} values.","focus")
        ri(n-1)
        key=a[n-1]
        j=n-2
        snap(s,a,[key["id"]],f"Insert key {key['value']}.","focus")
        while j>=0 and a[j]["value"] > key["value"]:
            moving=a[j]
            a[j+1]=moving
            snap(s,a,[moving["id"],key["id"]],f"Shift {moving['value']} right.","swap")
            j-=1
        a[j+1]=key
        snap(s,a,[key["id"]],f"Place {key['value']} here.","focus")
    ri(len(a))
    snap(s,a,[x["id"] for x in a],"Sorted.","done")
    return s

STEP_BUILDERS={
"Selection Sort":selection_steps,
"Bubble Sort":bubble_steps,
"Insertion Sort":insertion_steps,
"Merge Sort":merge_steps,
"Quick Sort":quick_steps,
"Recursive Bubble Sort":recursive_bubble_steps,
"Recursive Insertion Sort":recursive_insertion_steps,
}

def visualizer(name, nums):
    steps = STEP_BUILDERS[name](nums)
    payload = json.dumps(steps)
    count = len(nums)

    components.html(f"""
    <div id="sortviz" class="sv-root">
      <style>
        .sv-root{{
          font-family:Inter,ui-sans-serif,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
          color:#312a33;
          border:1px solid #eadce5;
          background:rgba(255,255,255,.94);
          border-radius:20px;
          padding:18px;
          box-sizing:border-box;
        }}
        .sv-top{{
          display:flex;align-items:center;justify-content:space-between;
          gap:12px;flex-wrap:wrap;margin-bottom:6px;
        }}
        .sv-caption{{font-size:13px;color:#7f7381;font-weight:650}}
        .sv-controls{{display:flex;gap:7px;flex-wrap:wrap}}
        .sv-btn{{
          border:1px solid #e2d4dc;background:white;color:#433a44;
          border-radius:10px;padding:8px 11px;font-weight:750;cursor:pointer;
        }}
        .sv-btn.primary{{background:#d86496;border-color:#d86496;color:white}}
        .sv-stage{{
          position:relative;
          height:215px;
          margin:14px 0 8px;
          border-top:1px solid #f0e5eb;
          border-bottom:1px solid #f0e5eb;
          overflow:hidden;
        }}
        .penguin{{
          position:absolute;
          top:43px;
          width:min(100px, calc((100% - 8px) / {count}));
          height:145px;
          transition:left .55s cubic-bezier(.2,.8,.2,1), transform .28s ease, filter .25s ease;
          transform:translateX(-50%);
          display:flex;
          justify-content:center;
          align-items:flex-start;
        }}
        .penguin img{{
          width:100%;
          max-width:90px;
          height:112px;
          object-fit:cover;
          border-radius:22px;
          mix-blend-mode:multiply;
          filter:saturate(.92) contrast(1.03);
          user-select:none;
          pointer-events:none;
        }}
        .value{{
          position:absolute;
          top:69px;
          left:50%;
          transform:translateX(-50%);
          min-width:32px;
          height:32px;
          padding:0 7px;
          border-radius:999px;
          background:rgba(255,255,255,.96);
          border:1px solid #dbcbd4;
          display:flex;
          align-items:center;
          justify-content:center;
          font-size:15px;
          font-weight:900;
          color:#2e2730;
          box-shadow:0 4px 10px rgba(103,73,90,.08);
        }}
        .index{{
          position:absolute;
          bottom:0;
          left:50%;
          transform:translateX(-50%);
          font-size:11px;color:#9b8f99;font-weight:700;
        }}
        .penguin.active{{
          transform:translateX(-50%) translateY(-11px);
          filter:drop-shadow(0 8px 11px rgba(199,85,136,.17));
        }}
        .penguin.swap{{
          transform:translateX(-50%) translateY(-15px) scale(1.035);
        }}
        .penguin.done .value{{
          border-color:#c985a5;
          background:#fff3f8;
        }}
        .sv-note{{
          min-height:44px;
          display:flex;align-items:center;
          padding:9px 12px;
          border-radius:12px;
          background:#fff6fa;
          color:#584d58;
          font-size:14px;
          line-height:1.45;
        }}
        .sv-progress{{height:4px;background:#f2e5ec;border-radius:20px;margin-top:12px;overflow:hidden}}
        .sv-progress>div{{height:100%;background:#d86496;transition:width .2s ease}}
        .sv-count{{font-size:11px;color:#9c9099;text-align:right;margin-top:6px}}
        @media(max-width:520px){{
          .sv-stage{{height:190px}}
          .penguin{{top:48px;height:125px}}
          .penguin img{{max-width:70px;height:92px}}
          .value{{top:56px;height:28px;min-width:28px;font-size:13px}}
        }}
      </style>

      <div class="sv-top">
        <div class="sv-caption">Watch the penguins become the sorted array</div>
        <div class="sv-controls">
          <button class="sv-btn" id="prev" type="button">Back</button>
          <button class="sv-btn primary" id="play" type="button">Play</button>
          <button class="sv-btn" id="next" type="button">Next</button>
          <button class="sv-btn" id="reset" type="button">Reset</button>
        </div>
      </div>

      <div class="sv-stage" id="stage"></div>
      <div class="sv-note" id="note"></div>
      <div class="sv-progress"><div id="progress"></div></div>
      <div class="sv-count" id="count"></div>

      <script>
        (() => {{
          const steps = {payload};
          const stage = document.getElementById("stage");
          const note = document.getElementById("note");
          const progress = document.getElementById("progress");
          const count = document.getElementById("count");
          const playBtn = document.getElementById("play");
          const penguinUrl = {json.dumps(PENGUIN_URL)};
          let idx = 0;
          let timer = null;

          const ids = steps[0].items.map(x => x.id);
          ids.forEach(id => {{
            const wrap = document.createElement("div");
            wrap.className = "penguin";
            wrap.dataset.id = id;

            const img = document.createElement("img");
            img.src = penguinUrl;
            img.alt = "3D penguin array element";
            wrap.appendChild(img);

            const value = document.createElement("div");
            value.className = "value";
            wrap.appendChild(value);

            const index = document.createElement("div");
            index.className = "index";
            wrap.appendChild(index);

            stage.appendChild(wrap);
          }});

          function render(){{
            const s = steps[idx];
            const posById = {{}};
            s.items.forEach((item, pos) => posById[item.id] = pos);

            ids.forEach(id => {{
              const el = stage.querySelector(`[data-id="${{id}}"]`);
              const pos = posById[id];
              const item = s.items[pos];
              el.style.left = `${{((pos + .5) / s.items.length) * 100}}%`;
              el.querySelector(".value").textContent = item.value;
              el.querySelector(".index").textContent = pos;
              el.className = "penguin";
              if (s.active.includes(id)) el.classList.add("active");
              if (s.active.includes(id) && s.state === "swap") el.classList.add("swap");
              if (s.state === "done") el.classList.add("done");
            }});

            note.textContent = s.note;
            progress.style.width = `${{((idx+1)/steps.length)*100}}%`;
            count.textContent = `Step ${{idx+1}} of ${{steps.length}}`;
          }}

          function stop(){{
            if(timer) clearInterval(timer);
            timer = null;
            playBtn.textContent = "Play";
          }}

          document.getElementById("next").addEventListener("click", () => {{
            stop();
            idx = Math.min(idx + 1, steps.length - 1);
            render();
          }});
          document.getElementById("prev").addEventListener("click", () => {{
            stop();
            idx = Math.max(idx - 1, 0);
            render();
          }});
          document.getElementById("reset").addEventListener("click", () => {{
            stop();
            idx = 0;
            render();
          }});
          playBtn.addEventListener("click", () => {{
            if(timer){{
              stop();
              return;
            }}
            playBtn.textContent = "Pause";
            timer = setInterval(() => {{
              if(idx >= steps.length - 1){{
                stop();
                return;
              }}
              idx++;
              render();
            }}, 1050);
          }});

          render();
        }})();
      </script>
    </div>
    """, height=370, scrolling=False)

def home():
    st.markdown("""
    <div class="hero">
      <div class="hero-kicker">Java sorting, visually</div>
      <h1>Learn sorting without making it feel like homework.</h1>
      <div class="hero-copy">
        Choose one topic. First understand the idea, then watch the values physically move,
        and only after that read the Java code.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("Choose a topic")

    cards = [
        ("Selection Sort","Find the minimum and move it forward."),
        ("Bubble Sort","Swap neighboring values until the largest bubbles right."),
        ("Insertion Sort","Insert one value at a time into a sorted prefix."),
        ("Merge Sort","Split, sort, then merge."),
        ("Quick Sort","Partition around a pivot."),
        ("Recursive Bubble Sort","Bubble once, then recurse."),
        ("Recursive Insertion Sort","Sort n - 1, then insert the last value."),
        ("Arrays","Review indexing before sorting."),
    ]
    cols = st.columns(2)
    for i,(name,desc) in enumerate(cards):
        with cols[i%2]:
            st.markdown(f"""
            <div class="home-card">
              <div class="home-card-title">{name}</div>
              <div class="home-card-copy">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Open {name}", key=f"open_{name}"):
                st.session_state.page = name
                st.rerun()

def top_nav(name):
    c1,c2 = st.columns([1,5])
    with c1:
        if st.button("Back to topics", key=f"back_{name}"):
            st.session_state.page="Home"
            st.rerun()
    with c2:
        st.markdown(f'<div class="navline">Sorting / {name}</div>', unsafe_allow_html=True)

def arrays_page():
    top_nav("Arrays")
    st.markdown("""
    <div class="hero">
      <div class="hero-kicker">Foundation</div>
      <h1>Arrays</h1>
      <div class="hero-copy">
        An array is a fixed row of values. Every value has an index, and Java starts indexing at 0.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("Read an array")
    nums=[7,4,1,5,3]
    fake_steps=[{
        "items":[{"id":f"p{i}","value":v} for i,v in enumerate(nums)],
        "active":[],
        "note":"Each penguin is one array element. The small number below it is the index.",
        "state":"normal"
    }]
    # Re-use a simpler one-frame visual.
    payload=json.dumps(fake_steps)
    components.html(f"""
    <div style="font-family:Inter,Arial;border:1px solid #eadce5;background:white;border-radius:20px;padding:18px;">
      <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;padding:12px 0 6px;">
        {''.join([f'<div style="text-align:center"><div style="position:relative;width:90px;height:120px"><img src="{PENGUIN_URL}" style="width:90px;height:105px;object-fit:cover;border-radius:20px;mix-blend-mode:multiply"><div style="position:absolute;left:50%;top:62px;transform:translateX(-50%);background:white;border:1px solid #dcced6;border-radius:999px;padding:5px 10px;font-weight:800">{v}</div></div><div style="font-size:12px;color:#8f838d">index {i}</div></div>' for i,v in enumerate(nums)])}
      </div>
    </div>
    """, height=200)

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("Java")
    st.code("""int[] arr = {7, 4, 1, 5, 3};

System.out.println(arr[0]);  // 7
System.out.println(arr[2]);  // 1

arr[2] = 10;                // change index 2

for (int i = 0; i < arr.length; i++) {
    System.out.println(arr[i]);
}""", language="java")
    st.markdown("""
    <div class="note">
      The three things you need before sorting are: index access, arr.length, and swapping values.
    </div>
    """, unsafe_allow_html=True)

def algorithm_page(name):
    top_nav(name)
    info=DATA[name]

    st.markdown(f"""
    <div class="hero">
      <div class="hero-kicker">Sorting algorithm</div>
      <h1>{name}</h1>
      <div class="hero-copy">{info["summary"]}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="clean-card">
      <strong>Remember it like this:</strong>
      <div style="margin-top:.35rem;color:#695d68">{info["memory"]}</div>
      <div class="metric-row">
        <div class="metric">
          <div class="metric-label">Time</div>
          <div class="metric-value">{info["time"]}</div>
        </div>
        <div class="metric">
          <div class="metric-label">Extra space</div>
          <div class="metric-value">{info["space"]}</div>
        </div>
        <div class="metric">
          <div class="metric-label">Stable</div>
          <div class="metric-value">{info["stable"]}</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("Watch it happen")
    raw = st.text_input(
        "Array",
        "7, 4, 1, 5, 3",
        key=f"nums_{name}",
        help="Use 2 to 8 integers separated by commas.",
    )
    nums=parse_nums(raw)
    if nums is None:
        st.error("Enter 2 to 8 whole numbers separated by commas.")
        nums=[7,4,1,5,3]
    visualizer(name, nums)

    st.markdown('<div class="section"></div>', unsafe_allow_html=True)
    st.subheader("Now read the Java")
    st.markdown(f"""
    <div class="cat-note">
      <img src="{CAT_URL}" alt="Animated cat teacher from LottieFiles">
      <div class="cat-note-text">
        Read the code only after watching the movement above. Match each loop or condition
        to the exact action you just watched.
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.code(JAVA[name], language="java")

    with st.expander("Explain the important lines"):
        for code_line, meaning in EXPLAIN[name]:
            st.markdown(
                f"<div style='padding:.65rem 0;border-bottom:1px solid #f0e6ec'>"
                f"<code>{html.escape(code_line)}</code>"
                f"<div style='margin-top:.3rem;color:#6f626d'>{html.escape(meaning)}</div>"
                f"</div>",
                unsafe_allow_html=True
            )

    st.markdown(f"""
    <div class="note">
      If you can explain this sentence without looking at the code, you understand the algorithm:
      <strong>{info["memory"]}</strong>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="small-credit">
      Character artwork references: LottieFiles free animation assets. The site uses the character images
      only as learning mascots; sorting motion is created by the visualizer itself.
    </div>
    """, unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page="Home"

if st.session_state.page=="Home":
    home()
elif st.session_state.page=="Arrays":
    arrays_page()
else:
    algorithm_page(st.session_state.page)
