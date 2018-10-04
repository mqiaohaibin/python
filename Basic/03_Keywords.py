# Python keyword is a unique programming term intended to perform some action. There are as
# many as 33 such keywords in Python, each serving a different purpose.
#
# Keywords are special words which are reserved and have a specific meaning. Python has a set
# keywords that cannot be used as variables in programs.
#
# All keywords in Python are case sensitive.
#
# Here is a list of the Python keywords.
# False     def         if          raise       None        del         import      return
# True      elif        in          try         and         else        is          while
# as        except      lambda      with        assert      finally     nonlocal    yield
# break     for         not         class       from        or          continue    golbal
# pass
#
import keyword
print(keyword.kwlist)

# Python Identifiers are user-defined names to represent a variable, function, class, module
# or any other object. If you assign some name to a programmable entity in Python, then it is
# nothing but technically called an identifier.
#
# Python language lays down a set of rules for programmers to create meaningful identifier.
# 1. To form an identifier, use a sequence of letters either in lowercase (a to z) or
# uppercase (A to Z). However, you can also mix up digits (0 to 9) or an underscore (_) while
# writing an identifier.
# 2. You can't use digits to begin an identifier name. It'll lead to the syntax eror.
# 3. Also, the Keywords are reserved, so you should not use them as identifiers.
# 4. Python Identifiers can also not have special characters ['.', '@', '#', '$', '%'] in their
# formation. These symbols are forbidden.
# 5. Python doc says that you can have an identifier with unlimited length. But it is just the
# half truth. Using a large name (more than 79 chars) would lead to the violation of a rule set
# by the PEP-8 standard.

# Another useful method to check if an identifier is valid or not is by calling the
# str.isidentifier() function. But it is only available in Python 3.0 and onwards.

print("techbeamers".isidentifier())
print("1techbeamers".isidentifier())
print("techbeamers.com".isidentifier())
print("techbeamers_com".isidentifier())

# Best Practices For Identifier Naming.
# Better have class names starting with a captial letter. All other identifiers should begin
# with a lowercase letter.
# Declare private identifiers by using the ('_') underscore as their first letter.
# Avoid using names with only one character. Instead, make meaningful names.
# You can use underscore to combile multiple words to form a sensible name.

# A variable in Python represents an entity whose value can change as and when required.
# Conceptually, it is a memory location which holds the actual value. And we can retrieve
# the value from our code by querying the entity.
#
# But it requires assigning a label to that memory location so that we can reference it. And
# we call it as a variable in the programming terms.
#
# 1. Variables don't require declaration. However, you must initialize them before use.
# 2. A assignment expression will lead to the following actions.
#   1> Creating of an object to represent the value.
#   2> If the variable doesn't exist, then it'll get created.
#   3> Association of the variable with the object, so that it can refer the value.
# 3. Whenever the expression changes, Python associates a new object (a chunk of memory) to
# the variable for referencing that value. And the old one goes to the garbage collector.
# 4. Also, for optimization, Python builds a cache and reuses some of the immutable objects,
# such as small integers and strings.
# 5. An object is just a region of memory which can hold the following.
#   1> The actual object values.
#   2> A type designator to reflect the object type.
#   3> The reference counter which determines when it's OK to reclaim the object.
# 6. It's the object which has a type, not the variable. However, a variable can hold objects
# of different types as and when required.
