open Core

let cnt = ref 0
let prev = ref Int.max_value
let cur = ref Int.max_value

let compare_lines new_number =
  prev := !cur;
  cur := int_of_string new_number;
  if !prev < !cur then cnt := !cnt + 1
;;

let () =
  let lines = In_channel.read_lines "input.txt" in
  List.iter ~f:compare_lines lines;
  printf "%d\n" !cnt
;;
