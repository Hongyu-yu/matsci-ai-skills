#!/usr/bin/env python3
"""
Random Creativity Prompt Generator

Generates random creativity prompts from different categories to spark
brainstorming and break through creative blocks.

Usage:
    python random_prompt.py [category]

Categories:
    constraint, perspective, time, scale, removal, addition, industry,
    reversal, random-word, absurd, combination, emotional, all

Examples:
    python random_prompt.py                    # Random from any category
    python random_prompt.py constraint         # Random constraint prompt
    python random_prompt.py perspective        # Random perspective prompt
    python random_prompt.py --list             # List all categories
"""

import random
import sys

# Prompt categories and their prompts
PROMPTS = {
    "constraint": [
        "What if you had zero budget?",
        "What if you could only spend $100?",
        "What if you had unlimited budget but only 24 hours?",
        "What if you had to do this alone?",
        "What if you could use only one tool?",
        "What if you couldn't talk to customers?",
        "What if customers couldn't talk to you?",
        "What if you had no internet?",
        "What if customers had no internet?",
        "What if you couldn't use electricity?",
    ],
    "perspective": [
        "How would a 5-year-old approach this?",
        "How would a teenager solve this?",
        "How would someone over 80 do this?",
        "How would your younger self handle this?",
        "How would a complete beginner approach this?",
        "How would an absolute expert handle this?",
        "How would someone from a different field solve this?",
        "How would your biggest competitor do this?",
        "How would Steve Jobs approach this?",
        "How would a detective solve this?",
        "How would an artist approach this?",
        "How would a scientist handle this?",
    ],
    "time": [
        "What if you had to launch tomorrow?",
        "What if you had 10 years?",
        "What if this had to work for 100 years?",
        "What if you only had one shot at this?",
        "What if this happened 10x more often?",
        "What if this happened once in a lifetime?",
        "What if this was instant?",
        "What if this took years?",
    ],
    "scale": [
        "What if this were 10x bigger?",
        "What if this were 100x smaller?",
        "What if this served one person perfectly?",
        "What if this served the entire planet?",
        "What if you could only make one?",
        "What if you had to make a million?",
        "What if usage increased 1000x overnight?",
        "What if only 10 people ever used this?",
    ],
    "removal": [
        "What if you removed the most popular feature?",
        "What if this had only one button?",
        "What if you removed all customization?",
        "What if there was no user interface?",
        "What if there was no sign-up?",
        "What if there were no instructions?",
        "What if customers never saw pricing?",
        "What if there was no branding?",
    ],
    "addition": [
        "What if this included entertainment?",
        "What if this included education?",
        "What if this created community?",
        "What if this predicted the future?",
        "What if this happened at a party?",
        "What if this happened in a crisis?",
        "What if this was a game?",
        "What if this was art?",
    ],
    "industry": [
        "How would a restaurant approach this?",
        "How would a theme park design this?",
        "How would a hospital approach this?",
        "How would a luxury hotel do this?",
        "How would a military unit organize this?",
        "How would a video game approach this?",
        "How would a news organization do this?",
        "How would a concert venue handle this?",
        "How would Disney handle this?",
        "How would Amazon approach this?",
        "How would Tesla design this?",
        "How would Netflix do this?",
    ],
    "reversal": [
        "What if customers paid you to take this away?",
        "What if you started at the end and worked backwards?",
        "What if the problem was actually the solution?",
        "What if you did the opposite of best practices?",
        "What if customers did what you do?",
        "What if you did what customers do?",
        "What if the newest employee led this?",
        "What if your harshest critic designed this?",
    ],
    "random-word": [
        "Connect your challenge to: FOREST (growth, ecosystem, layers)",
        "Connect your challenge to: OCEAN (depth, waves, tides, exploration)",
        "Connect your challenge to: MOUNTAIN (climbing, peak, view, challenge)",
        "Connect your challenge to: RIVER (flow, obstacles, journey)",
        "Connect your challenge to: BRIDGE (connection, crossing, support)",
        "Connect your challenge to: GARDEN (cultivation, growth, harvest)",
        "Connect your challenge to: MIRROR (reflection, reversal, truth)",
        "Connect your challenge to: COMPASS (direction, navigation, guidance)",
        "Connect your challenge to: DANCE (rhythm, partnership, flow)",
        "Connect your challenge to: COOKING (ingredients, process, timing)",
        "Connect your challenge to: FLYING (lift, navigation, speed, altitude)",
        "Connect your challenge to: BUILDING (foundation, structure, construction)",
    ],
    "absurd": [
        "What if this was made entirely of chocolate?",
        "What if this had to work on the moon?",
        "What if aliens were your customers?",
        "What if this was invisible?",
        "What if this happened in your dreams?",
        "What if this was a living creature?",
        "What if this could read minds?",
        "What if time ran backwards for this?",
    ],
    "combination": [
        "Combine your challenge with: Social media",
        "Combine your challenge with: Subscription boxes",
        "Combine your challenge with: Video games",
        "Combine your challenge with: Dating apps",
        "Combine your challenge with: Food delivery",
        "Combine your challenge with: Escape rooms",
        "Combine your challenge with: Music festivals",
        "Combine your challenge with: Libraries",
        "Combine your challenge with: Coffee shops",
        "Combine your challenge with: Fitness trackers",
    ],
    "emotional": [
        "What would make this delightful?",
        "What would make users cry (happy tears)?",
        "What would make this feel like magic?",
        "What would make users laugh?",
        "What would make users feel powerful?",
        "What would make users feel safe?",
        "What would make users feel connected?",
        "What would make users feel smart?",
    ],
}


def get_random_prompt(category=None):
    """
    Get a random prompt from the specified category or all categories.

    Args:
        category: Category name or None for random from all

    Returns:
        Tuple of (category_name, prompt_text)
    """
    if category and category != "all":
        if category not in PROMPTS:
            available = ", ".join(PROMPTS.keys())
            raise ValueError(f"Unknown category: {category}\nAvailable categories: {available}")
        selected_category = category
        prompt = random.choice(PROMPTS[category])
    else:
        # Random from all categories
        selected_category = random.choice(list(PROMPTS.keys()))
        prompt = random.choice(PROMPTS[selected_category])

    return selected_category, prompt


def list_categories():
    """Print all available categories with counts."""
    print("\nAvailable Categories:\n")
    for category, prompts in PROMPTS.items():
        count = len(prompts)
        print(f"  {category:15} ({count:2} prompts)")
    print("\n  all             (all categories)")
    print(f"\nTotal prompts: {sum(len(p) for p in PROMPTS.values())}")
    print("\nUsage: python random_prompt.py [category]")


def get_multiple_prompts(count=3, category=None):
    """
    Get multiple random prompts without repetition.

    Args:
        count: Number of prompts to generate
        category: Category name or None for random from all

    Returns:
        List of tuples of (category_name, prompt_text)
    """
    if category and category != "all":
        if category not in PROMPTS:
            raise ValueError(f"Unknown category: {category}")
        prompts_pool = PROMPTS[category].copy()
        random.shuffle(prompts_pool)
        return [(category, p) for p in prompts_pool[:count]]
    else:
        # Get from all categories
        all_prompts = [(cat, prompt) for cat, prompts in PROMPTS.items() for prompt in prompts]
        random.shuffle(all_prompts)
        return all_prompts[:count]


def main():
    """Main entry point for command-line usage."""
    # Parse arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()

        if arg in ["-h", "--help", "help"]:
            print(__doc__)
            return

        if arg in ["-l", "--list", "list"]:
            list_categories()
            return

        if arg in ["-m", "--multiple", "multiple"]:
            # Get multiple prompts
            count = 3
            category = None
            if len(sys.argv) > 2:
                try:
                    count = int(sys.argv[2])
                except ValueError:
                    category = sys.argv[2]
                if len(sys.argv) > 3:
                    try:
                        count = int(sys.argv[3])
                    except ValueError:
                        pass

            prompts = get_multiple_prompts(count, category)
            print(f"\n{count} Random Prompts:\n")
            for i, (cat, prompt) in enumerate(prompts, 1):
                print(f"{i}. [{cat.upper()}] {prompt}")
            print()
            return

        # Assume it's a category
        category = arg
    else:
        category = None

    # Get and display random prompt
    try:
        cat, prompt = get_random_prompt(category)
        print(f"\n[{cat.upper()}]")
        print(f"\n{prompt}\n")
    except ValueError as e:
        print(f"\nError: {e}\n")
        list_categories()
        sys.exit(1)


if __name__ == "__main__":
    main()
