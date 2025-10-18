def get_digit_counts(text):
    counts = {}
    for ch in text:
        if ch.isdigit():
            num = int(ch)
            counts[num] = counts.get(num, 0) + 1
    return counts


def top3_digits(text):
    counts = get_digit_counts(text)
    if not counts:
        return {}

    sorted_items = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    top = sorted_items[:3]
    return dict(sorted(top))


if __name__ == '__main__':
    s = "987654321098765432109876543210987654"
    s2 = "000111222333444555666777888999000111222"

    all_counts = get_digit_counts(s2)
    top3 = top3_digits(s2)

    print("Cловарь -> ", all_counts)
    print("3 самых частых -> ", top3)