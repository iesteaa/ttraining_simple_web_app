# My First Frontend Journey With an Agent, and What It Taught Me

This document is both a personal note and a practical guide. It records my first time building a frontend, when I used a Copilot agent plan created specifically by iino-san, my team leader, to guide frontend work in a more disciplined way.

The idea behind that agent plan was good: inspect the existing UI assets first, ask for major design choices one step at a time, identify what should be shared or created once, and end with a handoff-ready implementation plan that stayed aligned with the project architecture. In other words, the agent was supposed to help me work inside the system, not invent a new one.

I did not understand that well enough at first.

## What Happened

I started building the frontend with the agent too early, before the foundation was ready. I assumed the agent could fill the gaps for me, but that assumption was the mistake.

When a frontend project does not yet have a solid baseline, the agent has too much freedom. It will try to be helpful, and that often means making design decisions on its own. The result can look clean, but it may drift away from the intended architecture.

The clearest example is [frontend/src/App.vue](../frontend/src/App.vue). In that file, the root app already contains page-level UI decisions such as a branded top bar, product naming, subtitle copy, and a documentation link. None of that is technically wrong. The problem is that the root shell is carrying decisions that should have been delayed until the project had a clearer system to follow.

## Why That Was a Problem

The agent plan was designed to work inside a prepared foundation. Without that foundation, the boundaries become too easy to ignore in practice, even if they are written clearly.

Here is what was missing when I started:

1. A clear visual baseline, including theme, spacing, typography, radius, and responsive rules.
2. Existing assets and references that the agent could inspect before creating anything new.
3. A defined route structure and a minimal app shell.
4. A shared component map that separates what should be reusable from what is page-specific.
5. A state matrix covering loading, empty, error, validation, disabled, and long-content cases.
6. Realistic mock data or a concrete data contract.
7. Clear rules for icons, illustrations, and layout dimensions.

Without those things, the agent had to guess. And when an agent guesses in a greenfield frontend, it tends to fill the gaps with page-local decisions that are hard to undo later.

## What I Learned

The main lesson is simple: an agent should not be the starting point for frontend architecture. It should be used after the foundation exists.

That means I should prepare the frontend first, then let the agent help with reproduction and implementation inside that structure. The foundation should make the boundaries enforceable, not merely descriptive.

I also learned that the root app must stay minimal. If App becomes the place where all visual decisions are stored, the shell stops being a neutral container and becomes a design dump. That makes the frontend harder to maintain, harder to reuse, and harder for the next developer or agent to understand.

## How Frontend Should Be Prepared

If I were starting again, I would prepare the project in this order:

1. Define the product goal, user flow, and the main problem the frontend must solve.
2. Inspect the existing assets, shared patterns, and design-system references before creating new UI.
3. Lock the route structure and keep the app shell minimal.
4. Decide which components should be shared and which ones are allowed to remain page-specific.
5. Set a visual baseline early so the agent does not invent its own style.
6. Prepare the key UI states and realistic mock data before building the final screen.
7. Only after that, start using the agent for implementation and refinement.

This sequence matters because it prevents the agent from becoming a substitute for architecture.

## When the Agent Should Start Being Used

The agent is most useful after three things are already true:

1. The project direction is clear.
2. The shell and design constraints are already established.
3. There is enough reference material for the agent to follow instead of inventing.

At that point, the agent can speed up implementation without drifting the codebase. Before that point, it is easy for the agent to create polished output that is structurally wrong.

## Final Checklist

Before I ask an agent to build a frontend again, I should make sure these are ready:

1. The product purpose and user journey are written down.
2. The design boundaries are explicit and technically grounded.
3. The route structure works and the root app stays simple.
4. The baseline visual rules are known.
5. The shared components and page-specific areas are separated.
6. The expected states are listed and accounted for.
7. The data source or mock is realistic enough to support the UI.
8. The icon and illustration rules are clear.
9. The agent is only used after the system is ready for it.

## Closing Reflection

This experience taught me that a frontend does not become good because the output looks finished. It becomes good when the structure behind the output is disciplined.

The agent created by iino-san was meant to help us reproduce frontend code in a cleaner, more aligned way. That still makes sense to me. What I misunderstood was the timing. The agent is a multiplier, not a foundation.

So the real lesson for me is this: prepare the frontend first, then let the agent work inside that structure. That is how the output stays useful, maintainable, and aligned with the architecture the team actually wants.
