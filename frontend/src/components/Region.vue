<template>
    <span>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
        <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
        </svg>
    </span>
    <div :class="{hidden: !show}"  class="dropdown-item-content absolute top-9 w-32 transition ease-in-out delay-150 z-50">
        <ul  class="bg-primary-700 py-2 px-4">
        <li class="plx-2 py-2">
            <a href="{% url 'index' %}?category=1">全部</a>
        </li>
        <li class="plx-2 py-2">
            <a href="{% url 'index' %}?category=1&region=1">中国大陆</a>
        </li>
        <li class="plx-2 py-2">
            <a href="{% url 'index' %}?category=1&region=2">中国香港</a>
        </li>
        <li class="plx-2 py-2">
            <a href="{% url 'index' %}?category=1&region=3">中国台湾</a>
        </li>
        <li class="plx-2 py-2">
            <a href="{% url 'index' %}?category=1&region=4">美国</a>
        </li>
        <li class="plx-2 py-2">
            <a href="{% url 'index' %}?category=1&region=5">韩国</a>
        </li>
        <li class="plx-2 py-2">
            <a href="{% url 'index' %}?category=1&region=6">日本</a>
        </li>
        <li class="plx-2 py-2">
            <a href="{% url 'index' %}?category=1&region=7">其他</a>
        </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'Region',
    props: ['cagegory_name'],
}
</script>