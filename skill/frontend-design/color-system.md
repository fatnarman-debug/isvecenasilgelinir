# Color System Reference

> Color theory principles, selection process, and decision-making guidelines.
> **No memorized hex codes - learn to THINK about color.**

---

## 1. Color Theory Fundamentals

### The Color Wheel

```
                    YELLOW
                      │
           Yellow-    │    Yellow-
           Green      │    Orange
              ╲       │       ╱
               ╲      │      ╱
    GREEN ─────────── ● ─────────── ORANGE
               ╱      │      ╲
              ╱       │       ╲
           Blue-      │    Red-
           Green      │    Orange
                      │
                     RED
                      │
                   PURPLE
                  ╱       ╲
             Blue-         Red-
             Purple        Purple
                  ╲       ╱
                    BLUE
```

### Color Relationships

| Scheme | How to Create | When to Use |
|--------|---------------|-------------|
| **Monochromatic** | Pick ONE hue, vary only lightness/saturation | Minimal, professional, cohesive |
| **Analogous** | Pick 2-3 ADJACENT hues on wheel | Harmonious, calm, nature-inspired |
| **Complementary** | Pick OPPOSITE hues on wheel | High contrast, vibrant, attention |
| **Split-Complementary** | Base + 2 colors adjacent to complement | Dynamic but balanced |
| **Triadic** | 3 hues EQUIDISTANT on wheel | Vibrant, playful, creative |

### How to Choose a Scheme:
1. **What's the project mood?** Calm → Analogous. Bold → Complementary.
2. **How many colors needed?** Minimal → Monochromatic. Complex → Triadic.
3. **Who's the audience?** Conservative → Monochromatic. Young → Triadic.

---

## 2. The 60-30-10 Rule

### Distribution Principle

```
60% PRIMARY (Background / Base)
├── Provides the main context
└── Usually neutral (whites, grays, darks)

30% SECONDARY (Support / Layout)
├── Adds visual interest
└── Usually brand colors or muted tones

10% ACCENT (Action / Focus)
├── Drives user behavior
└── High contrast, vibrant (CTAs, links)
```

### Implementation Tip
If you use Tailwind, don't just pick `bg-blue-500`. 
Define them as CSS variables: `--primary`, `--secondary`, `--accent`.

---

## 3. Psychological Color Context

What colors usually mean to users:

| Color | Mood / Industry | Common Use |
|-------|-----------------|------------|
| **Blue** | Trust, Tech, Finance | Enterprise apps, dashboards |
| **Green** | Growth, Health, Success | Fintech, fitness, eco-apps |
| **Red** | Urgent, Danger, Passion | Errors, food, entertainment |
| **Purple** | Luxury, Creative, Mystery | Design tools, premium services |
| **Yellow** | Warning, Energy, Happy | Utility, delivery, kids' apps |
| **Orange** | Friendly, Playful, Action | E-commerce, modern SaaS |

---

## 4. Accessibility in Color

### Contrast Ratios (WCAG 2.1)
- **Normal Text**: 4.5:1 (AA) or 7:1 (AAA)
- **Large Text**: 3:1 (AA) or 4.5:1 (AAA)
- **UI Components**: 3:1 (AA)

### Color Blindness Considerations
- Never rely on color alone to convey meaning (e.g., use icons + color for error states).
- Use patterns or textures in charts if possible.
- Check designs using a grayscale filter.

---

## 5. Selection Decision Tree

**Step 1: Identify Industry**
- Finance/Legal → Deep Blue / Gray
- Creative/Startup → Vibrant Purple / Gradient
- Health/Nature → Soft Green / Earth Tones

**Step 2: Define "Temperature"**
- Clean/Tech → Cool (Blues/Cyans)
- Friendly/Human → Warm (Oranges/Yellows)

**Step 3: Pick the Accent**
- Needs to "pop" against the 60% and 30%.
- If background is dark, use light/vibrant accent.
- If background is light, use saturated accent.

---

## 6. Neutral Palettes

Neutrals are the most important part of any UI.

- **Warm Neutrals**: (Ivory, Cream, Sand) → Feel organic and high-end.
- **Cool Neutrals**: (Slate, Zinc, Steel) → Feel modern and tech-focused.
- **Pure Neutrals**: (White, Black, Gray) → Feel utilitarian and clinical.

---

## 7. Anti-Patterns to Avoid

- ❌ **The "AI Default"**: Dark background + neon purple accent.
- ❌ **The "Vibrant Mess"**: Too many high-saturation colors (leads to fatigue).
- ❌ **The "Invisible Link"**: Accent color with poor contrast against background.
- ❌ **The "Rainbow Table"**: Every row in a different color.

---

> **Design Tip**: Pick your colors in grayscale first to ensure hierarchy and contrast work, then add hue.
