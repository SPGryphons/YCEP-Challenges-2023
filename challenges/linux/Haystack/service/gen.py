fake_flag1 = "NOT_A_FLAG{this_is_a_fake_flag}"
fake_flag2 = "FAKE_FLAG{this_is_a_fake_flag}"
fake_flag3 = "FLAG{this_is_a_fake_flag}"

for i in range(1000):
    with open(f"./flags/file{i}", "w") as f:
        f.write(fake_flag1 if i % 3 == 0 else fake_flag2 if i % 3 == 1 else fake_flag3)

