# How to Debug Shopping Cart Function - Step by Step

## Step 1: Read and Understand Requirements
1. **Read the problem statement carefully**
   - Function takes `cart` (dictionary) and `action` (dictionary)
   - Cart format: `{"product_id": quantity}`
   - Action has: `type`, `product_id`, and optionally `quantity`
   - Three operations: "add", "remove", "change"

2. **Understand expected behavior**
   - Add: Increase quantity or create new entry
   - Remove: Delete item completely from cart
   - Change: Set new quantity or remove if 0

## Step 2: Analyze Current Code Line by Line

### Add Operation Analysis:
```python
if action["type"] == "add":
    if product_id not in cart:        # ❌ WRONG: Checking NOT IN first
        cart[product_id] += action["quantity"]  # ❌ WRONG: Can't += on non-existent key
    else:
        cart[product_id] = action["quantity"]   # ❌ WRONG: Should be += for existing items
```

**Problems identified:**
- Logic is backwards (checking NOT IN first)
- Trying to += on non-existent key causes KeyError
- Not accumulating quantity for existing items

### Remove Operation Analysis:
```python
elif action["type"] == "remove":
    cart[product_id] = 0    # ❌ WRONG: Setting to 0, not removing
```

**Problems identified:**
- Setting quantity to 0 instead of removing the key
- Not checking if product exists first

### Change Operation Analysis:
```python
elif action["type"] == "change" and action.get("quantity", 0) > 0:
    cart[product_id] = action["quantity"] - 1    # ❌ WRONG: Why subtract 1?
```

**Problems identified:**
- Subtracting 1 for no logical reason
- Condition prevents handling quantity = 0 case
- Not removing item when quantity should be 0

## Step 3: Fix Each Operation

### Fix Add Operation:
```python
if product_id in cart:              # ✅ Check if exists first
    cart[product_id] += action["quantity"]  # ✅ Add to existing
else:
    cart[product_id] = action["quantity"]   # ✅ Create new entry
```

### Fix Remove Operation:
```python
if product_id in cart:              # ✅ Check if exists first
    del cart[product_id]            # ✅ Actually remove the key
```

### Fix Change Operation:
```python
if "quantity" in action:            # ✅ Check if quantity provided
    if action["quantity"] > 0:
        cart[product_id] = action["quantity"]  # ✅ Set new quantity
    else:
        if product_id in cart:      # ✅ Remove if quantity ≤ 0
            del cart[product_id]
```

## Step 4: Test Mental Cases

### Test Add:
- New item: Should create entry
- Existing item: Should add to current quantity

### Test Remove:
- Existing item: Should completely remove
- Non-existent item: Should do nothing (no error)

### Test Change:
- Positive quantity: Should set new value
- Zero/negative quantity: Should remove item
- Non-existent item with positive quantity: Should create entry

## Step 5: Code Review Checklist

- ✅ No KeyError possibilities
- ✅ All three operations work correctly
- ✅ Edge cases handled (non-existent products)
- ✅ Logic flows make sense
- ✅ Code is readable and maintainable

## General Debugging Tips:

1. **Read error messages carefully** - KeyError usually means accessing non-existent dictionary key
2. **Trace through code with sample data** - Walk through each line with example inputs
3. **Check edge cases** - What happens with empty cart, non-existent products, zero quantities?
4. **Verify logic flow** - Does the if/else structure make sense?
5. **Test incrementally** - Fix one operation at a time and test it
