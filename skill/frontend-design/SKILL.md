# Frontend Design System

> ⚠️ **MANDATORY**: READ `decision-trees.md` AND `guidelines.md` BEFORE PROCEEDING.

🎯 **Selective Reading Rule (MANDATORY)**:
DO NOT read all files in this directory. Only read the specific file relevant to the task you are performing (e.g., if working on animations, read `animation-guide.md`).

🔧 **Runtime Scripts**:
- `.agent/skills/frontend-design/scripts/setup.sh`: Initializes the design system environment.
- `.agent/skills/frontend-design/scripts/validate.sh`: Validates design choices against system rules.

⚠️ **CRITICAL: ASK BEFORE ASSUMING (MANDATORY)**
When User Prompt is Vague, ASK:
- "What is the primary industry/niche?"
- "What is the target audience (age, tech-savviness)?"
- "Is there a specific emotional response you want (trust, excitement, calm)?"
- "Do you have existing brand colors or should I generate a palette?"
- "Light mode, dark mode, or both?"

⛔ **DEFAULT TENDENCIES TO AVOID (ANTI-SAFE HARBOR):**
- DO NOT default to a "dark mode with purple/violet accents" palette.
- DO NOT use the same generic "modern/clean" design for every project.
- DO NOT skip the constraint analysis step.

---

## 1. Constraint Analysis (ALWAYS FIRST)
Before proposing any design, analyze:
- **Technical constraints**: Framework, performance requirements, browser support.
- **Timeline**: Is this a quick prototype or a production-ready application?
- **Audience**: Professional? Casual? Accessible for elderly/impaired?

## 2. UX Psychology Principles
### Emotional Design Levels
- **Visceral**: Immediate aesthetic reaction (first 500ms).
- **Behavioral**: Ease of use and performance (interaction).
- **Reflective**: Long-term satisfaction and brand alignment.

### Trust Building
- Use familiar patterns (e.g., login at top right).
- Maintain consistency across all views.
- Provide clear feedback for all user actions.

## 3. Layout Principles
### Golden Ratio (φ = 1.618)
Use the golden ratio for:
- Sizing major components (e.g., main content vs. sidebar).
- Defining font size relationships (e.g., H1 = 1.618 * H2).

### 8-Point Grid Concept
- All margins, paddings, and sizes should be multiples of 8px.
- Use 4px for fine-grained adjustments.
- Ensures vertical rhythm and alignment.

## 4. Color Principles
### 60-30-10 Rule
- **60% Primary**: Neutral background or base.
- **30% Secondary**: Support color, defines the mood.
- **10% Accent**: Call-to-action (CTA), highlights, focus states.

### Selection Process
- Refer to `color-system.md` for context-based choices.

## 5. Typography Principles
### Pairing Concept
- Use a maximum of TWO font families.
- Pair a Serif (headings) with a Sans-Serif (body) for classic looks.
- Use a single variable font with multiple weights for modern, high-performance looks.

### Readability Rules
- Line length: 45-75 characters per line.
- Line height: 1.4 to 1.6 for body text.
- Contrast: Check WCAG compliance (AA minimum).

## 6. Visual Effects Principles
### Glassmorphism (When Appropriate)
- Use on floating UI elements (modals, dropdowns).
- Requires background blur (backdrop-filter) and thin borders.

### Shadow Hierarchy
- Soft, layered shadows (multiple box-shadow values).
- High elevation = larger, softer shadow.
- Avoid heavy, dark black shadows (#000).

### Gradient Usage
- Subtle gradients only (limited color stops).
- Mimic natural lighting sources (top-down).

## 7. Animation Principles
### Timing Concept
- UI feedback: 100-200ms.
- Page transitions: 300-500ms.
- Use `cubic-bezier(.4, 0, .2, 1)` (standard ease) as default.

### Performance
- Animate only `transform` and `opacity`.
- Use `will-change` sparingly.

## 8. "Wow Factor" Checklist
- [ ] Micro-interactions on buttons/links.
- [ ] Subtle scroll animations (reveal-on-scroll).
- [ ] Custom loading states (skeleton screens).
- [ ] Deliberate use of whitespace (breathing room).
- [ ] High-quality, context-aware imagery/icons.

## 9. Anti-Patterns (What NOT to Do)
### ❌ Lazy Design Indicators:
- Default Tailwind colors without modification.
- "Coming Soon" sections.
- Stock photos with watermarks or low resolution.

### ❌ AI Tendency Patterns (AVOID!):
- Neon purple everything.
- Over-animated elements that slow down the user.
- Floating "bubbles" in every background.

### ❌ Dark Patterns (Unethical):
- Hidden checkboxes for newsletters.
- Confusopoly pricing tables.
- Forced continuity (hidden cancel buttons).

## 10. Decision Process Summary
1. Analyze industry and constraints.
2. ASK user for missing details.
3. Define 60-30-10 palette (`color-system.md`).
4. Select typography hierarchy (`typography-system.md`).
5. Choose layout grid and spacing.
6. Apply visual effects and motion (`motion-graphics.md`).
7. Validate against accessibility standards.

### Reference Files
- `color-system.md`: How to think about color.
- `typography-system.md`: How to think about text.
- `motion-graphics.md`: How to think about movement.
- `decision-trees.md`: Logical flow for design choices.

### Related Skills
- `app-builder`: Implementation and framework specifics.
- `api-patterns`: Interaction design for data-heavy apps.

---

## Post-Design Workflow
1. Run `validate.sh` on the proposed CSS/Components.
2. Provide a "Design Rationale" to the user explaining WHY these choices were made (using the principles above).

## 5. Next.js 16+ Modern Form Patterns

### The <Form> Component Advantage
The new Next.js `<Form>` component (from `next/form`) significantly improves UX by:
- **Prefetching**: Prefetches the target page on hover.
- **Client-Side Navigation**: Enhances search/filter forms without full page reloads.
- **Progressive Enhancement**: Works even before JS hydration.

### Implementation Example (Search Bar)
```tsx
import Form from 'next/form';

export default function Search() {
  return (
    <Form action="/search" className="relative">
      <input 
        name="q" 
        className="w-full rounded-lg border px-4 py-2 focus:ring-2 focus:ring-accent"
        placeholder="Search..."
      />
      <button type="submit" className="absolute right-2 top-2">
        🔍
      </button>
    </Form>
  );
}
```

### When to use <Form> vs. standard <form>:
- **Use `<Form>`**: For GET requests that navigate (search, filters, sorting).
- **Use `<form>`**: For POST/PUT/DELETE requests (auth, data mutation, file uploads).
