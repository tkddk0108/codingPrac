-- 코드를 작성해주세요
select i.id, count(j.Parent_ID) as CHILD_COUNT
from Ecoli_data i left join Ecoli_data j
    on i.id = j.Parent_ID
group by 1
