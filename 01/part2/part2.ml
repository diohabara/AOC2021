open Core

let cnt = ref 0
let prev = ref Int.max_value
let cur = ref Int.max_value

let rec list_of_each_three_numbers_sum numbers =
  match numbers with
  | a :: b :: c :: rest ->
    let new_sum = a + b + c in
    new_sum :: list_of_each_three_numbers_sum ([ b; c ] @ rest)
  | _ -> []
;;

let handle_line new_number =
  prev := !cur;
  cur := new_number;
  if !prev < !cur then cnt := !cnt + 1
;;

let () =
  let lines = In_channel.read_lines "input.txt" in
  let numbers = List.map ~f:int_of_string lines in
  let sums = list_of_each_three_numbers_sum numbers in
  sums |> List.iter ~f:handle_line;
  printf "%d\n" !cnt
;;
