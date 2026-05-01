# Motion Graphics & UI Transitions

> Guidelines for high-end movement and animated visual elements.
> **Movement should feel fluid, not robotic.**

---

## 1. The Physics of Motion

### Mass and Inertia
- **Heavy elements** (large modals, full sections): Move slower, have more "momentum."
- **Light elements** (icons, tooltips, buttons): Move faster, feel more "zippy."

### Natural Arcs
Elements rarely move in perfectly straight lines in nature.
- Use **Slight Curves** for elements moving across large distances.
- Use **Quadratic Bezier** curves for more natural feeling paths.

---

## 2. Advanced Easing Library

Use these custom bezier values for a more "premium" feel than default eases.

| Style | CSS `cubic-bezier` | Description |
|-------|--------------------|-------------|
| **The "Snap"** | `.2, 0, 0, 1` | Very fast start, long deceleration. Great for buttons. |
| **The "Glide"** | `.4, 0, .2, 1` | Balanced, smooth movement. Best for general UI. |
| **The "Elevate"** | `.3, 0, .1, 1` | Feels like it's lifting off the page. Best for cards. |
| **The "Elastic"** | `.17, .67, .83, .67` | Playful bounce (use sparingly). |

---

## 3. Micro-interactions

Small animations that respond to user action.

### Button States
- **Hover**: Subtle lift (y-translation) or background shift.
- **Active (Click)**: Slight scale down (0.98) to mimic physical compression.
- **Loading**: Pulse or subtle spinner that doesn't shift layout.

### Input Focus
- Border color transition (200ms).
- Label floating (if using that pattern).
- Subtle shadow "glow" (layered shadows).

---

## 4. Page Transitions

### The "Slide-and-Fade"
1. Old content fades out and slides slightly left (-20px).
2. New content fades in and slides from right (20px to 0).
3. **Duration**: 400ms total.

### The "Shared Element" (Hero Transition)
- An image or heading stays visible and "morphs" from list-view to detail-view.
- Use libraries like `framer-motion` (LayoutID) for this.

---

## 5. Reveal-on-Scroll Patterns

### Principles
- **Don't overdo it**: Only reveal key sections.
- **Directional**: Elements should reveal from the direction they are "coming from."
- **Stagger**: Reveal multiple items (cards, list) one after another.

### Tailwind / Intersection Observer Example:
```html
<!-- Base Class -->
<div class="opacity-0 translate-y-8 transition-all duration-700">
  <!-- Revealed Class (via JS) -->
  <div class="opacity-100 translate-y-0">
  </div>
</div>
```

---

## 6. Loading States & Skeletons

### The "Shimmer" Effect
- Use a linear gradient that moves from left to right.
- **Speed**: 1.5s - 2s loop.
- **Color**: Very subtle contrast (e.g., Gray 200 to Gray 300).

### Skeleton Shapes
- Match the exact layout of the content that is coming.
- Rounded corners should match the final components.

---

## 7. Motion Anti-Patterns

- ❌ **The "Drunk" element**: Too much bounce/elasticity.
- ❌ **The "Stagger Lag"**: Staggering so many items that the last one takes seconds to appear.
- ❌ **The "Wall of Motion"**: Animating everything on the page at once.
- ❌ **The "Sudden Stop"**: Using `ease-in` for elements entering (they should decelerate).

---

## 8. Motion Decision Matrix

| Question | If YES | If NO |
|----------|--------|-------|
| Does it block user action? | Use Skeleton Screen | No animation needed |
| Is it a secondary detail? | Use simple Fade (200ms) | No animation needed |
| Is it for "Delight"? | Use custom ease + scale | Use standard ease |
| Is it a large viewport change? | Use 400ms + Slide | Use 200ms + Fade |
