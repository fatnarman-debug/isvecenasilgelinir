# Animation Guidelines Reference

> Principles for creating purposeful, performant, and delightful movement in UI.
> **Motion should explain, not just entertain.**

---

## 1. Core Philosophy of Motion

Motion in digital interfaces serves three primary purposes:
1. **Continuity**: Explaining where an element came from and where it is going.
2. **Feedback**: Confirming that a user action was registered.
3. **Focus**: Directing the user's attention to what matters most.

### The "Goldilocks" Rule
- Too little motion = Interface feels "stiff" or broken.
- Too much motion = Interface feels distracting or nauseating.
- **Just right** = Motion feels natural and invisible until noticed.

---

## 2. Timing and Duration Guidelines

Standard durations for common UI tasks:

| Duration | Use Case |
|----------|----------|
| **100ms - 150ms** | Micro-interactions (hover, toggle, small scale changes) |
| **200ms - 300ms** | Small transitions (dropdowns, tooltips, checkmark reveals) |
| **300ms - 450ms** | Large transitions (sidebar slides, modal fades, view changes) |
| **500ms+** | Complex orchestrations or branding animations |

### Rule of Area
The larger the element and the further it moves, the slower it should be. A small button hover should be instant (100ms); a full-page modal should be deliberate (400ms).

---

## 3. Easing Functions (The "Soul" of Motion)

Never use `linear` transitions for UI elements unless it's a progress bar.

| Easing Type | CSS Value | Feel |
|-------------|-----------|------|
| **Ease-In** | `cubic-bezier(0.4, 0, 1, 1)` | Accelerates. Use for elements **leaving** the screen. |
| **Ease-Out** | `cubic-bezier(0, 0, 0.2, 1)` | Decelerates. Use for elements **entering** the screen. |
| **Ease-In-Out** | `cubic-bezier(0.4, 0, 0.2, 1)` | Standard. Use for elements moving **within** the screen. |
| **Overshoot** | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Bouncy. Use for playful, "physical" interactions. |

---

## 4. Performance Standards

To maintain 60fps (or 120fps), follow these technical constraints:

### ✅ DO animate:
- `transform: translate()` (Position)
- `transform: scale()` (Size)
- `transform: rotate()` (Rotation)
- `opacity` (Transparency)

### ❌ AVOID animating:
- `width`, `height`, `top`, `left` (Triggers Reflow)
- `margin`, `padding` (Triggers Reflow)
- `box-shadow` (Expensive to paint)
- `filter` (blur, brightness - use sparingly)

---

## 5. Implementation Patterns (Tailwind Examples)

### The "Standard" Reveal
```html
<div class="transition-all duration-300 ease-out opacity-0 translate-y-4 hover:opacity-100 hover:translate-y-0">
  <!-- Content -->
</div>
```

### The "Springy" Button
```html
<button class="transition-transform duration-150 active:scale-95">
  Click Me
</button>
```

### Staggered List Entrance
When showing a list, delay each item slightly to create a "flow":
```html
<li class="animate-in fade-in slide-in-from-bottom-2 duration-300 delay-[100ms]">Item 1</li>
<li class="animate-in fade-in slide-in-from-bottom-2 duration-300 delay-[200ms]">Item 2</li>
<li class="animate-in fade-in slide-in-from-bottom-2 duration-300 delay-[300ms]">Item 3</li>
```

---

## 6. Accessibility in Motion

### Reduced Motion Support
Always respect the user's system preferences.
```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Safety Rules:
- Avoid flashing content (risk of seizures).
- Avoid excessive parallax or high-speed movement (risk of vertigo).
- Ensure all automated movement can be paused or disabled.

---

## 7. Motion Decision Tree

**Is the user interacting with an element?**
- **YES**: Keep it fast (<200ms). Use an overshoot ease for a "physical" feel.
- **NO (Auto-reveal)**: Keep it moderate (300-400ms). Use `ease-out`.

**Is it a primary action?**
- **YES**: Motion should be distinct/pronounced.
- **NO**: Motion should be subtle/muted.

**Is the content being replaced?**
- **YES**: Use a "Cross-fade" or "Slide + Fade" combo.
- **NO**: Use a simple "Opacity" or "Scale" transition.

---

## 8. Anti-Patterns to Avoid

- ❌ **The "Stutter"**: Animating properties that cause layout shifts (like `height`).
- ❌ **The "Sluggish"**: Making simple interactions take longer than 300ms.
- ❌ **The "Wobble"**: Using excessive "spring" physics on professional corporate tools.
- ❌ **The "Ghost"**: Animating elements that have no logical entry/exit point.

---

> **Design Tip**: The best animations are the ones that feel like they are obeying the laws of physics within your app's digital space.
