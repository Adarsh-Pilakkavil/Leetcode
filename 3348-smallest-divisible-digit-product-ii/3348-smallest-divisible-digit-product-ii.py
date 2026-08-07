class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        needed_2s = 0
        needed_3s = 0
        needed_5s = 0
        needed_7s = 0
        remaining_target = t
        while remaining_target % 2 == 0:
            needed_2s += 1
            remaining_target //= 2
        while remaining_target % 3 == 0:
            needed_3s += 1
            remaining_target //= 3
        while remaining_target % 5 == 0:
            needed_5s += 1
            remaining_target //= 5
        while remaining_target % 7 == 0:
            needed_7s += 1
            remaining_target //= 7
        if remaining_target != 1:
            return "-1"
        digit_offerings = {
            1: (0, 0, 0, 0), 
            2: (1, 0, 0, 0), 
            3: (0, 1, 0, 0), 
            4: (2, 0, 0, 0), 
            5: (0, 0, 1, 0), 
            6: (1, 1, 0, 0), 
            7: (0, 0, 0, 1), 
            8: (3, 0, 0, 0), 
            9: (0, 2, 0, 0), 
        }
        def has_enough_space(empty_slots, need_2, need_3, need_5, need_7):
            if need_5 + need_7 > empty_slots: 
                return False
            remaining = empty_slots - need_5 - need_7
            slots_needed_for_3s = (need_3 + 1) // 2
            if slots_needed_for_3s > remaining:
                return False
            max_2s_possible = (remaining - slots_needed_for_3s) * 3
            if need_3 % 2 == 1:
                max_2s_possible += 1
            if need_2 > max_2s_possible:
                return False
            return True
        def build_with_restriction(cur_slot, is_restricted, need_2, need_3, need_5, need_7, clipboard):
            if cur_slot == len(num):
                return need_2 == 0 and need_3 == 0 and need_5 == 0 and need_7 == 0
            start_digit = 1
            if is_restricted:
                start_digit = max(1, int(num[cur_slot]))
            for digit in range(start_digit, 10):
                still_restricted = is_restricted and (digit == int(num[cur_slot]))
                gives_2, gives_3, gives_5, gives_7 = digit_offerings[digit]

                new_need_2 = max(0, need_2 - gives_2)
                new_need_3 = max(0, need_3 - gives_3)
                new_need_5 = max(0, need_5 - gives_5)
                new_need_7 = max(0, need_7 - gives_7)

                empty_slots_left = len(num) - cur_slot - 1

                if not has_enough_space(empty_slots_left, new_need_2, new_need_3, new_need_5, new_need_7):
                    continue
                clipboard.append(str(digit))
                if not still_restricted:
                    found_rest_of_number = build_unrestricted(empty_slots_left, new_need_2, new_need_3, new_need_5, new_need_7, clipboard)
                else:
                    found_rest_of_number = build_with_restriction(
                        cur_slot + 1, still_restricted, new_need_2, new_need_3, new_need_5, new_need_7, clipboard
                    )
                if found_rest_of_number:
                    return True
                clipboard.pop()
            
            return False
     
        def build_unrestricted(empty_slots, need_2, need_3, need_5, need_7, clipboard):
            if empty_slots == 0:
                return need_2 == 0 and need_3 == 0 and need_5 == 0 and need_7 == 0
            
            if not has_enough_space(empty_slots, need_2, need_3, need_5, need_7):
                return False
            
            for digit in range(1, 10):
                gives_2, gives_3, gives_5, gives_7 = digit_offerings[digit]

                new_need_2 = max(0, need_2 - gives_2)
                new_need_3 = max(0, need_3 - gives_3)
                new_need_5 = max(0, need_5 - gives_5)
                new_need_7 = max(0, need_7 - gives_7)
                if not has_enough_space(empty_slots - 1, new_need_2, new_need_3, new_need_5, new_need_7):
                    continue
                clipboard.append(str(digit))

                found_rest_of_number = build_unrestricted(empty_slots - 1, new_need_2, new_need_3, new_need_5, new_need_7, clipboard)

                if found_rest_of_number:
                    return True
                
                clipboard.pop()
            
            return False

        shared_clipboard = []
        same_length_answer = build_with_restriction(
            cur_slot=0, 
            is_restricted=True, 
            need_2=needed_2s, need_3=needed_3s, need_5=needed_5s, need_7=needed_7s,
            clipboard=shared_clipboard
        )

        if same_length_answer:
            return "".join(shared_clipboard)
        

        new_length = len(num) + 1

        while True:
            shared_clipboard = []
            ans = build_unrestricted(new_length, needed_2s, needed_3s, needed_5s, needed_7s, shared_clipboard)

            if ans:
                return "".join(shared_clipboard)

            new_length += 1